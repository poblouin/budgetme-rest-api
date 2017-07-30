from rest_framework.filters import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from budgetme.apps.transactions.filters import TransactionFilter
from budgetme.apps.transactions.models import Account, Transaction
from budgetme.apps.transactions.renderers import AccountJSONRenderer, TransactionJSONRenderer
from budgetme.apps.transactions.serializers import AccountSerializer, TransactionSerializer


class AccountViewSet(ModelViewSet):
    queryset = Account.objects.select_related('user')
    permission_classes = (IsAuthenticated,)
    renderer_classes = (AccountJSONRenderer,)
    serializer_class = AccountSerializer

    def get_queryset(self):
        return self.request.user.accounts.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


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
