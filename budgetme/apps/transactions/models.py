from django.db import models

from budgetme.apps.core.models import TimestampedModel


class Account(TimestampedModel):
    CHEQUE = 'CH'
    ACCOUNT_TYPE_CHOICES = (
        (CHEQUE, 'Cheque'),
    )

    name = models.CharField(max_length=30, unique=True)
    account_type = models.CharField(max_length=2, choices=ACCOUNT_TYPE_CHOICES)

    user = models.ForeignKey('core.User', on_delete=models.CASCADE, related_name='accounts')


class Transaction(TimestampedModel):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    user = models.ForeignKey('core.User', on_delete=models.CASCADE, related_name='transactions')
    transaction_category = models.ForeignKey('types.TransactionCategory', on_delete=models.CASCADE, related_name='+')
    account = models.ForeignKey('Account', related_name='transactions', on_delete=models.CASCADE)


# class ScheduledTransaction(models.Model):
#     description = models.CharField(max_length=50)
#     start_date = models.DateField()
#     end_date = models.DateField(null=True, blank=True)
#
#     user = models.ForeignKey('core.User', on_delete=models.CASCADE, related_name='transactions')
#     transaction_category = models.ForeignKey('TransactionCategory', on_delete=models.CASCADE, related_name='+')
#     frequency = models.ForeignKey('Frequency', on_delete=models.CASCADE, related_name='+')
#     account = models.ForeignKey('Account', related_name='scheduled_transactions')
