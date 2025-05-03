from django.urls import path
from .views import RegisterView, ProfileView, subscribe_ott

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('subscribe/', subscribe_ott, name='subscribe-ott'), 
]