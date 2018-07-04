from decimal import Decimal
from django.core.validators import MinValueValidator
from django.db import models

from budgetme.apps.core.constants import DAILY, WEEKLY, BI_WEEKLY, MONTHLY
from budgetme.apps.core.models import TimestampedModel


class Transaction(TimestampedModel):
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    date = models.DateField()
    description = models.CharField(max_length=100)

    user = models.ForeignKey('core.User', on_delete=models.CASCADE, related_name='transactions')
    transaction_category = models.ForeignKey('types.TransactionCategory', on_delete=models.CASCADE, related_name='+')

    def __str__(self):
        return '{}$ on {}'.format(self.amount, self.date)

    def __repr__(self):
        return 'Transaction<amount={}, date={}>'.format(self.amount, self.date)


class ScheduledTransaction(TimestampedModel):
    SCHEDULE_FREQUENCY_CHOICES = (
        (DAILY, DAILY),
        (WEEKLY, WEEKLY),
        (BI_WEEKLY, BI_WEEKLY),
        (MONTHLY, MONTHLY)
    )

    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    description = models.CharField(max_length=100)
    frequency = models.CharField(max_length=9, choices=SCHEDULE_FREQUENCY_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField(default=None, null=True)

    user = models.ForeignKey('core.User', on_delete=models.CASCADE, related_name='scheduled_transactions')
    transaction_category = models.ForeignKey('types.TransactionCategory', on_delete=models.CASCADE, related_name='+')

    def __str__(self):
        return '{}$ each {}, starting on {} ending on {}'.format(self.amount, self.frequency, self.start_date, self.end_date)

    def __repr__(self):
        return 'ScheduledTransaction<amount={}, frequency={}, start_date={}>'.format(self.amount, self.frequency, self.start_date)
