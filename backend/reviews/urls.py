from django.urls import path
from .views import ReviewListCreateView, ReviewDetailView
from .views import ReviewLikeToggleView

urlpatterns = [
    path('', ReviewListCreateView.as_view(), name='review-list'),
    path('<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
    path('<int:pk>/like-toggle/', ReviewLikeToggleView.as_view(), name='review-like-toggle'),
]