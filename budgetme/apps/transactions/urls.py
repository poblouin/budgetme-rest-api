from django.urls import path, include
from rest_framework.routers import DefaultRouter

from budgetme.apps.transactions.views import TransactionViewSet, ScheduledTransactionViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'transaction', TransactionViewSet)
router.register(r'scheduled-transaction', ScheduledTransactionViewSet)

app_name = 'transactions'
urlpatterns = [
    path('', include(router.urls)),
]
