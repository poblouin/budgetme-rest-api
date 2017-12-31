import django_filters

from budgetme.apps.types.models import TransactionCategory


class TransactionCategoryFilter(django_filters.rest_framework.FilterSet):
    budget_name = django_filters.CharFilter(name='budget__name', lookup_expr='iexact')

    class Meta:
        model = TransactionCategory
        fields = ['budget_name']
