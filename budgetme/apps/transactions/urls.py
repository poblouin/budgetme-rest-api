from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from budgetme.apps.transactions.views import AccountViewSet, TransactionViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'account', AccountViewSet)
router.register(r'transaction', TransactionViewSet)

app_name = 'transactions'
urlpatterns = [
    url(r'^', include(router.urls)),
]
