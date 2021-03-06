import django_filters

from budgetme.apps.types.models import TransactionCategory


class TransactionCategoryFilter(django_filters.rest_framework.FilterSet):
    budget_name = django_filters.CharFilter(field_name='budget__name', lookup_expr='exact')

    class Meta:
        model = TransactionCategory
        fields = ['budget_name']
