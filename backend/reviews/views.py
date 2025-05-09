from rest_framework import status, generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Review, ReviewLike, ReviewComment, ReviewReaction
from .serializers import ReviewSerializer, ReviewCommentSerializer, ReviewLikeSerializer, ReviewReactionSerializer
from .permissions import IsOwnerOrReadOnly
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


# ✅ 리뷰 목록 조회 및 리뷰 작성
class ReviewListCreateView(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # 인증된 사용자만 작성 가능, 나머지는 읽기만 가능

    # Swagger 문서: 리뷰 목록 조회
    @swagger_auto_schema(
        operation_summary="리뷰 목록 조회",
        operation_description="영화 ID (movie)를 기준으로 리뷰를 필터링할 수 있습니다. 예: `/api/reviews/?movie=1`",
        manual_parameters=[
            openapi.Parameter(
                'movie',
                openapi.IN_QUERY,
                description="필터링할 영화의 ID",
                type=openapi.TYPE_INTEGER
            )
        ],
        responses={200: ReviewSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    # Swagger 문서: 리뷰 작성
    @swagger_auto_schema(
        operation_summary="리뷰 작성",
        operation_description="특정 영화에 대해 평점과 코멘트를 작성합니다. 평점은 1~5 사이여야 합니다.",
        request_body=ReviewSerializer,
        responses={201: ReviewSerializer}
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    # 쿼리 파라미터로 전달된 movie ID에 따라 필터링된 리뷰 목록 반환
    def get_queryset(self):
        movie_id = self.request.query_params.get('movie')
        if movie_id:
            return Review.objects.filter(movie_id=movie_id)
        return Review.objects.all()

    # 리뷰 작성 시 작성자를 현재 로그인한 사용자로 설정
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# ✅ 개별 리뷰 조회 / 수정 / 삭제
class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]  # 작성자만 수정/삭제 가능

    @swagger_auto_schema(operation_summary="리뷰 상세 조회")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="리뷰 수정",
        request_body=ReviewSerializer
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="리뷰 삭제")
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


# ✅ 리뷰 좋아요 기능 (토글 방식)
class ReviewLikeToggleView(APIView):
    permission_classes = [IsAuthenticated]  # 인증된 사용자만 가능

    @swagger_auto_schema(
        operation_summary="리뷰 좋아요 토글",
        operation_description="리뷰에 좋아요 또는 좋아요 취소를 토글합니다.",
        responses={
            200: openapi.Response(description="좋아요 취소됨", examples={"application/json": {"liked": False}}),
            201: openapi.Response(description="좋아요 등록됨", examples={"application/json": {"liked": True}})
        }
    )
    def post(self, request, pk):
        try:
            review = Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            return Response({'detail': '리뷰를 찾을 수 없습니다.'}, status=404)

        # 이미 좋아요한 경우 → 삭제(좋아요 취소), 그렇지 않으면 등록
        like, created = ReviewLike.objects.get_or_create(user=request.user, review=review)

        if not created:
            like.delete()
            return Response({'liked': False}, status=200)
        else:
            return Response({'liked': True}, status=201)


# ✅ 댓글 목록 조회 + 댓글 작성
class ReviewCommentListCreateView(generics.ListCreateAPIView):
    serializer_class = ReviewCommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # 특정 리뷰의 댓글만 조회
    def get_queryset(self):
        review_id = self.kwargs.get('review_id')
        return ReviewComment.objects.filter(review_id=review_id)

    @swagger_auto_schema(
        operation_summary="댓글 목록 조회",
        operation_description="특정 리뷰의 댓글 목록을 조회합니다.",
        responses={200: ReviewCommentSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="댓글 작성",
        operation_description="리뷰에 댓글을 작성합니다. content 필드만 입력하세요.",
        request_body=ReviewCommentSerializer,
        responses={201: ReviewCommentSerializer}
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    # 댓글 저장 시 현재 로그인한 사용자 + 해당 리뷰를 명시적으로 저장
    def perform_create(self, serializer):
        review_id = self.kwargs.get('review_id')
        review = Review.objects.get(pk=review_id)
        serializer.save(user=self.request.user, review=review)


# ✅ 댓글 삭제 (작성자만 가능)
class ReviewCommentDestroyView(generics.DestroyAPIView):
    queryset = ReviewComment.objects.all()
    serializer_class = ReviewCommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    @swagger_auto_schema(operation_summary="댓글 삭제")
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    
class ToggleReviewReaction(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, review_id, reaction_type):
        user = request.user
        is_like = reaction_type == 'like'

        try:
            review = Review.objects.get(id=review_id)
        except Review.DoesNotExist:
            return Response({"error": "리뷰를 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)

        reaction, created = ReviewReaction.objects.get_or_create(user=user, review=review)
        
        if not created:
            if reaction.is_like == is_like:
                # 같은 반응 → 취소
                reaction.delete()
                if is_like:
                    review.like_count -= 1
                else:
                    review.dislike_count -= 1
                review.save()
                return Response({"message": "반응이 취소되었습니다."})
            else:
                # 다른 반응 → 업데이트
                if is_like:
                    review.like_count += 1
                    review.dislike_count -= 1
                else:
                    review.dislike_count += 1
                    review.like_count -= 1
                reaction.is_like = is_like
                reaction.save()
                review.save()
                return Response({"message": "반응이 변경되었습니다."})
        else:
            # 새 반응 추가
            reaction.is_like = is_like
            reaction.save()
            if is_like:
                review.like_count += 1
            else:
                review.dislike_count += 1
            review.save()
            return Response({"message": "반응이 추가되었습니다."})