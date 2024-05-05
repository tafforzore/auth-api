from django.urls import path
from .views import UserAuthenticationView,UserRegistrationView

urlpatterns = [
    path('authentification/', UserAuthenticationView.as_view(), name='user-authentication'),
    path('registration/', UserRegistrationView.as_view(), name='user-registration')
]