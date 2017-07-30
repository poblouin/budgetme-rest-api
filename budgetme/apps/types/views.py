from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from budgetme.apps.types.models import TransactionCategory
from budgetme.apps.types.renderers import TransactionCategoryJSONRenderer
from budgetme.apps.types.serializers import TransactionCategorySerializer


class TransactionCategoryViewSet(ModelViewSet):
    queryset = TransactionCategory.objects.select_related('user')
    permission_classes = (IsAuthenticated,)
    renderer_classes = (TransactionCategoryJSONRenderer,)
    serializer_class = TransactionCategorySerializer

    def get_queryset(self):
        return self.request.user.transaction_categories.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
