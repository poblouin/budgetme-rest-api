import datetime
import os

import dateutil
from django.core.management.base import BaseCommand
from raven import Client

from budgetme.apps.core.constants import WEEKLY, BI_WEEKLY, MONTHLY, DAILY
from budgetme.apps.transactions.models import ScheduledTransaction, Transaction
from config.settings.production import SENTRY_DSN

SENTRY_CLIENT = None
if os.environ.get('DJANGO_SETTINGS_MODULE') == 'config.settings.production':
    SENTRY_CLIENT = Client(SENTRY_DSN)


class Command(BaseCommand):
    help = 'If a scheduled transaction is due, this command will create a new transaction  in the database'

    def add_arguments(self, parser):
        # Add User param?
        pass

    def handle(self, *args, **options):
        total_created = 0
        total_ignored = 0
        scheduled_transactions = ScheduledTransaction.objects.all()
        for scheduled_transaction in scheduled_transactions:
            now = datetime.datetime.now().date()

            if scheduled_transaction.start_date > now:
                continue
            if scheduled_transaction.end_date and scheduled_transaction.end_date < now:
                continue

            scheduled_date = None
            if scheduled_transaction.frequency == DAILY:
                scheduled_date = now
            if scheduled_transaction.frequency == WEEKLY:
                scheduled_date = scheduled_transaction.start_date + datetime.timedelta(days=7)
            elif scheduled_transaction.frequency == BI_WEEKLY:
                scheduled_date = scheduled_transaction.start_date + datetime.timedelta(days=14)
            elif scheduled_transaction.frequency == MONTHLY:
                scheduled_date = scheduled_transaction.start_date + dateutil.relativedelta.relativedelta(months=1)

            if scheduled_date is None:
                self.stdout.write(self.style.ERROR('scheduled_date was None, this should not happen.'))
                if SENTRY_CLIENT:
                    SENTRY_CLIENT.captureMessage('scheduled_date was None, this should not happen.', level='error')
                total_ignored += 1
                continue

            if scheduled_date != now:
                continue

            success = self._create_transaction(scheduled_transaction)
            if success:
                total_created += 1
                if not scheduled_transaction.end_date or scheduled_date < scheduled_transaction.end_date:
                    try:
                        scheduled_transaction.start_date = scheduled_date
                        scheduled_transaction.save()
                    except Exception as ex:
                        self.stdout.write(self.style.ERROR('Could not save new scheduled transaction start_date: {}'.format(ex)))
                        if SENTRY_CLIENT:
                            SENTRY_CLIENT.captureMessage('Could not save new scheduled transaction start_date: {}'.format(ex), level='error')
            else:
                total_ignored += 1

        exit_msg = 'Scheduled transactions processed with success, {} transactions were created, {} ignored'.format(total_created, total_ignored)
        self.stdout.write(self.style.SUCCESS(exit_msg))
        if SENTRY_CLIENT:
            SENTRY_CLIENT.captureMessage(exit_msg, level='info')

    def _create_transaction(self, scheduled_transaction):
        now = datetime.datetime.now().date()

        try:
            transaction = Transaction(
                amount=scheduled_transaction.amount,
                description=scheduled_transaction.description,
                date=now,
                user=scheduled_transaction.user,
                transaction_category=scheduled_transaction.transaction_category,
            )
            transaction.save()
        except Exception as ex:
            self.stdout.write(self.style.ERROR('Could not create new transaction: {}'.format(ex)))
            if SENTRY_CLIENT:
                SENTRY_CLIENT.captureException()
            return False

        return True
