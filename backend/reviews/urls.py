from django.urls import path
from .views import (
    ReviewListCreateView,        # 리뷰 목록 조회 + 작성
    ReviewDetailView,            # 리뷰 상세 조회, 수정, 삭제
    ReviewLikeToggleView,        # 리뷰 좋아요 토글
    ReviewCommentListCreateView, # 리뷰에 대한 댓글 목록 및 작성
    ReviewCommentDestroyView     # 댓글 삭제
)

urlpatterns = [
    # ✅ 리뷰 전체 목록 조회 및 새 리뷰 작성
    # GET /api/reviews/?movie=1 → 특정 영화 리뷰 필터 가능
    # POST /api/reviews/
    path('', ReviewListCreateView.as_view(), name='review-list-create'),

    # ✅ 리뷰 상세 조회, 수정, 삭제
    # GET, PUT, DELETE /api/reviews/<pk>/
    path('<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),

    # ✅ 특정 리뷰에 대한 좋아요 토글
    # POST /api/reviews/<pk>/like/
    path('<int:pk>/like/', ReviewLikeToggleView.as_view(), name='review-like'),

    # ✅ 특정 리뷰에 대한 댓글 목록 조회 및 댓글 작성
    # GET, POST /api/reviews/<review_id>/comments/
    path('<int:review_id>/comments/', ReviewCommentListCreateView.as_view(), name='review-comment-list-create'),

    # ✅ 특정 댓글 삭제 (작성자 본인만 가능)
    # DELETE /api/reviews/comments/<pk>/
    path('comments/<int:pk>/', ReviewCommentDestroyView.as_view(), name='review-comment-delete'),
]