from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from budgetme.apps.types.filters import TransactionCategoryFilter
from budgetme.apps.types.models import TransactionCategory, Budget
from budgetme.apps.types.renderers import TransactionCategoryJSONRenderer, BudgetJSONRenderer
from budgetme.apps.types.serializers import TransactionCategorySerializer, BudgetSerializer


class BudgetViewSet(ModelViewSet):
    queryset = Budget.objects.select_related('user')
    permission_classes = (IsAuthenticated,)
    renderer_classes = (BudgetJSONRenderer,)
    serializer_class = BudgetSerializer

    def get_queryset(self):
        return self.request.user.budgets.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TransactionCategoryViewSet(ModelViewSet):
    queryset = TransactionCategory.objects.select_related('user')
    permission_classes = (IsAuthenticated,)
    renderer_classes = (TransactionCategoryJSONRenderer,)
    serializer_class = TransactionCategorySerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = TransactionCategoryFilter

    def get_queryset(self):
        return self.request.user.transaction_categories.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
