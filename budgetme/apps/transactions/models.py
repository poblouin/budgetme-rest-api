from django.db import models

from budgetme.apps.core.models import TimestampedModel


class Transaction(TimestampedModel):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.CharField(max_length=100)

    user = models.ForeignKey('core.User', on_delete=models.CASCADE, related_name='transactions')
    transaction_category = models.ForeignKey('types.TransactionCategory', null=True, on_delete=models.SET_NULL, related_name='+')
    # budget = models.ForeignKey('Budget', related_name='transactions', on_delete=models.DO_NOTHING)

    def __str__(self):
        return '{}$ on {}'.format(self.amount, self.date)

    def __repr__(self):
        return 'Transaction<amount={}, date={}>'.format(self.amount, self.date)

# class ScheduledTransaction(models.Model):
#     description = models.CharField(max_length=50)
#     start_date = models.DateField()
#     end_date = models.DateField(null=True, blank=True)
#
#     user = models.ForeignKey('core.User', on_delete=models.CASCADE, related_name='transactions')
#     transaction_category = models.ForeignKey('TransactionCategory', on_delete=models.CASCADE, related_name='+')
#     frequency = models.ForeignKey('Frequency', on_delete=models.CASCADE, related_name='+')
#     account = models.ForeignKey('Account', related_name='scheduled_transactions')
