from django.urls import path, include
from rest_framework.routers import DefaultRouter

from budgetme.apps.types.views import TransactionCategoryViewSet, BudgetViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'budget', BudgetViewSet)
router.register(r'transaction-category', TransactionCategoryViewSet)

app_name = 'types'
urlpatterns = [
    path('', include(router.urls)),
]
