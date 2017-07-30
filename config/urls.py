from django.conf.urls import include, url
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^api/v1/', include('budgetme.apps.core.urls', namespace='core')),
    url(r'^api/v1/', include('budgetme.apps.types.urls', namespace='types')),
    url(r'^api/v1/', include('budgetme.apps.transactions.urls', namespace='transactions')),

    url(r'^api/v1/token-auth', obtain_jwt_token),
]
