from django.conf.urls import url

from budgetme.apps.core.views import UserRetrieveUpdateAPIView, RegistrationAPIView

app_name = 'core'
urlpatterns = [
    url(r'^user/?$', UserRetrieveUpdateAPIView.as_view()),
    url(r'^users/?$', RegistrationAPIView.as_view()),
]
