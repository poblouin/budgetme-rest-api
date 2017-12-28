from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from budgetme.apps.transactions.filters import TransactionFilter
from budgetme.apps.transactions.models import Transaction
from budgetme.apps.transactions.renderers import TransactionJSONRenderer
from budgetme.apps.transactions.serializers import TransactionSerializer


class TransactionViewSet(ModelViewSet):
    queryset = Transaction.objects.select_related('user')
    permission_classes = (IsAuthenticated,)
    renderer_classes = (TransactionJSONRenderer,)
    serializer_class = TransactionSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = TransactionFilter

    def get_queryset(self):
        return self.request.user.transactions.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
