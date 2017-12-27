from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^api/v1/', include('budgetme.apps.core.urls', namespace='core')),
    url(r'^api/v1/', include('budgetme.apps.types.urls', namespace='types')),
    url(r'^api/v1/', include('budgetme.apps.transactions.urls', namespace='transactions')),

    url(r'^api/v1/obtain-token', obtain_jwt_token),
    url(r'^api/v1/refresh-token', refresh_jwt_token),
]
