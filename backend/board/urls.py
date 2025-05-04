from django.urls import path
from .views import (
    BoardPostListCreateView,
    BoardPostDetailView,
    BoardCommentListCreateView,
    BoardCommentDestroyView,
)

urlpatterns = [
    # 게시글 목록 조회 및 작성
    path('', BoardPostListCreateView.as_view(), name='boardpost-list-create'),

    # 게시글 상세 조회, 수정, 삭제
    path('<int:pk>/', BoardPostDetailView.as_view(), name='boardpost-detail'),

    # 댓글 목록 및 작성 (게시글에 종속됨)
    path('<int:post_id>/comments/', BoardCommentListCreateView.as_view(), name='boardcomment-list-create'),

    # 댓글 삭제 (작성자만)
    path('comments/<int:pk>/', BoardCommentDestroyView.as_view(), name='boardcomment-delete'),
]