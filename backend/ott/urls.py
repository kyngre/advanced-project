from django.urls import path
from .views import OTTListView

urlpatterns = [
    path('', OTTListView.as_view(), name='ott-list'),
]