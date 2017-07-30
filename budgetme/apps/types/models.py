from django.db import models

from budgetme.apps.core.models import TimestampedModel


class TransactionCategory(TimestampedModel):
    INCOME = 'IN'
    EXPENSE = 'EX'
    TRANSACTION_TYPE_CHOICES = (
        (INCOME, 'Income'),
        (EXPENSE, 'Expense')
    )

    name = models.CharField(max_length=30, unique=True)
    transaction_type = models.CharField(max_length=2, choices=TRANSACTION_TYPE_CHOICES)
    user = models.ForeignKey('core.User', on_delete=models.CASCADE, related_name='transaction_categories')
