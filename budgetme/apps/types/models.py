from decimal import Decimal
from django.core.validators import MinValueValidator
from django.db import models

from budgetme.apps.core.models import TimestampedModel


class Budget(TimestampedModel):
    WEEKLY = 'Weekly'
    MONTHLY = 'Monthly'
    BUDGET_FREQUENCY_CHOICES = (
        (WEEKLY, 'Weekly'),
        (MONTHLY, 'Monthly')
    )

    name = models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    budget_frequency = models.CharField(max_length=7, choices=BUDGET_FREQUENCY_CHOICES, default=WEEKLY)

    user = models.ForeignKey('core.User', on_delete=models.CASCADE, related_name='budgets')

    def __str__(self):
        return self.name

    def __repr__(self):
        return 'Budget<name={}>'.format(self.name)


class TransactionCategory(TimestampedModel):
    class Meta:
        verbose_name_plural = 'Transaction categories'

    name = models.CharField(max_length=30)

    user = models.ForeignKey('core.User', on_delete=models.CASCADE, related_name='transaction_categories')
    budget = models.ForeignKey('Budget', blank=False, null=True, on_delete=models.SET_NULL, related_name='transaction_categories')

    def __str__(self):
        return self.name

    def __repr__(self):
        return 'TransactionCategory<name={}>'.format(self.name)
