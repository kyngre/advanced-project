from django.urls import path
from .views import ReviewListCreateView, ReviewDetailView
from .views import ReviewLikeToggleView, ReviewCommentListCreateView, ReviewCommentDestroyView

urlpatterns = [
    path('', ReviewListCreateView.as_view(), name='review-list'),
    path('<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
    path('<int:pk>/like-toggle/', ReviewLikeToggleView.as_view(), name='review-like-toggle'),
    path('<int:review_id>/comments/', ReviewCommentListCreateView.as_view(), name='review-comments'),
    path('comments/<int:pk>/', ReviewCommentDestroyView.as_view(), name='review-comment-delete'),
]