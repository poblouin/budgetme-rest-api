import django_filters

from budgetme.apps.transactions.models import Transaction, ScheduledTransaction


class TransactionFilter(django_filters.rest_framework.FilterSet):
    from_date = django_filters.DateTimeFilter(field_name='date', lookup_expr='gte')
    to_date = django_filters.DateTimeFilter(field_name='date', lookup_expr='lte')
    transaction_category = django_filters.CharFilter(field_name='transaction_category__name', lookup_expr='exact')
    budget_name = django_filters.CharFilter(field_name='transaction_category__budget__name', lookup_expr='exact')

    class Meta:
        model = Transaction
        fields = ['date', 'from_date', 'to_date', 'transaction_category', 'budget_name']


class ScheduledTransactionFilter(django_filters.rest_framework.FilterSet):
    transaction_category = django_filters.CharFilter(field_name='transaction_category__name', lookup_expr='exact')
    budget_name = django_filters.CharFilter(field_name='transaction_category__budget__name', lookup_expr='exact')

    class Meta:
        model = ScheduledTransaction
        fields = ['start_date', 'end_date', 'transaction_category', 'budget_name']
