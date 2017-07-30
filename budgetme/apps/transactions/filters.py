import django_filters

from budgetme.apps.transactions.models import Transaction


class TransactionFilter(django_filters.rest_framework.FilterSet):
    from_date = django_filters.DateTimeFilter(name='date', lookup_expr='gte')
    to_date = django_filters.DateTimeFilter(name='date', lookup_expr='lte')
    transaction_category = django_filters.CharFilter(name='transaction_category__name', lookup_expr='iexact')
    transaction_type = django_filters.CharFilter(name='transaction_category__transaction_type', lookup_expr='iexact')

    class Meta:
        model = Transaction
        fields = ['date', 'from_date', 'to_date', 'transaction_category', 'transaction_type']