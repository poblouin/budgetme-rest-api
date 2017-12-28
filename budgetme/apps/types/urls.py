from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from budgetme.apps.types.views import TransactionCategoryViewSet, BudgetViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'budget', BudgetViewSet)
router.register(r'transaction-category', TransactionCategoryViewSet)

app_name = 'types'
urlpatterns = [
    url(r'^', include(router.urls)),
]
