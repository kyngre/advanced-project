from rest_framework import generics, permissions
from .models import BoardPost, BoardComment
from .serializers import BoardPostSerializer, BoardCommentSerializer
from rest_framework.permissions import IsAuthenticated
from reviews.permissions import IsOwnerOrReadOnly  # 기존 권한 재사용

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


# ✅ 게시글 목록 조회 + 작성
class BoardPostListCreateView(generics.ListCreateAPIView):
    queryset = BoardPost.objects.all().order_by('-created_at')
    serializer_class = BoardPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(
        operation_summary="게시글 목록 조회",
        operation_description="전체 커뮤니티 게시글 목록을 최신순으로 반환합니다.",
        responses={200: BoardPostSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="게시글 작성",
        operation_description="로그인한 사용자가 커뮤니티 게시글을 작성합니다.",
        request_body=BoardPostSerializer,
        responses={201: BoardPostSerializer}
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# ✅ 게시글 상세 조회 / 수정 / 삭제
class BoardPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BoardPost.objects.all()
    serializer_class = BoardPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    @swagger_auto_schema(operation_summary="게시글 상세 조회")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="게시글 수정", request_body=BoardPostSerializer)
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="게시글 삭제")
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


# ✅ 댓글 목록 조회 + 작성
class BoardCommentListCreateView(generics.ListCreateAPIView):
    serializer_class = BoardCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return BoardComment.objects.filter(post_id=post_id)

    @swagger_auto_schema(
        operation_summary="댓글 목록 조회",
        operation_description="특정 게시글에 달린 모든 댓글을 조회합니다.",
        responses={200: BoardCommentSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="댓글 작성",
        operation_description="특정 게시글에 대해 댓글을 작성합니다.",
        request_body=BoardCommentSerializer,
        responses={201: BoardCommentSerializer}
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def perform_create(self, serializer):
        post_id = self.kwargs['post_id']
        serializer.save(user=self.request.user, post_id=post_id)


# ✅ 댓글 삭제 (작성자만 가능)
class BoardCommentDestroyView(generics.DestroyAPIView):
    queryset = BoardComment.objects.all()
    serializer_class = BoardCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    @swagger_auto_schema(operation_summary="댓글 삭제")
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)