from rest_framework import generics, permissions
from .models import BoardPost, BoardComment
from .serializers import BoardPostSerializer, BoardCommentSerializer
from rest_framework.permissions import IsAuthenticated
from reviews.permissions import IsOwnerOrReadOnly  # 기존 리뷰에서 사용하던 권한 재활용

# ✅ 게시글 목록 조회 및 작성
class BoardPostListCreateView(generics.ListCreateAPIView):
    queryset = BoardPost.objects.all().order_by('-created_at')
    serializer_class = BoardPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# ✅ 게시글 조회/수정/삭제
class BoardPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BoardPost.objects.all()
    serializer_class = BoardPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


# ✅ 댓글 목록 조회 및 작성 (특정 게시글 대상)
class BoardCommentListCreateView(generics.ListCreateAPIView):
    serializer_class = BoardCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return BoardComment.objects.filter(post_id=post_id)

    def perform_create(self, serializer):
        post_id = self.kwargs['post_id']
        serializer.save(user=self.request.user, post_id=post_id)


# ✅ 댓글 삭제 (작성자만 가능)
class BoardCommentDestroyView(generics.DestroyAPIView):
    queryset = BoardComment.objects.all()
    serializer_class = BoardCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
