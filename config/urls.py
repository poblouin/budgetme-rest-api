from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

API_ROOT = 'api/v1/'

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),

    path(API_ROOT, include('budgetme.apps.core.urls', namespace='core')),
    path(API_ROOT, include('budgetme.apps.types.urls', namespace='types')),
    path(API_ROOT, include('budgetme.apps.transactions.urls', namespace='transactions')),

    path(API_ROOT + 'token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(API_ROOT + 'token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
