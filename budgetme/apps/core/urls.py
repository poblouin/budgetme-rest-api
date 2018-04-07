from django.urls import path

from budgetme.apps.core.views import UserRetrieveUpdateAPIView, RegistrationAPIView

app_name = 'core'
urlpatterns = [
    path('user', UserRetrieveUpdateAPIView.as_view()),
    path('users', RegistrationAPIView.as_view()),
]
