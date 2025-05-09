from rest_framework import serializers
from .models import Review, ReviewHistory, ReviewImage, ReviewLike, ReviewComment, ReviewReaction,  ReviewCommentReaction


class ReviewImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewImage
        fields = ['id', 'image', 'uploaded_at']
        read_only_fields = ['id', 'uploaded_at']

# ✅ 리뷰 Serializer: 영화에 대한 평점 및 코멘트 작성/조회
class ReviewSerializer(serializers.ModelSerializer):
    # 작성자의 username을 읽기 전용으로 노출
    user = serializers.ReadOnlyField(source='user.username')

    # 평점은 1~5 사이의 정수로 제한
    rating = serializers.IntegerField(
        min_value=1,
        max_value=5,
        help_text="평점은 1점에서 5점 사이의 값으로 입력해야 합니다."
    )

    is_spoiler = serializers.BooleanField(
        default=False,
        help_text="리뷰에 스포일러가 포함되었는지 여부"
    )

    # 좋아요 개수 계산용 read-only 필드
    like_count = serializers.SerializerMethodField(help_text="이 리뷰에 달린 좋아요 수")

    is_edited = serializers.SerializerMethodField(help_text="리뷰가 수정된 적이 있는지 여부")

    images = ReviewImageSerializer(many=True, read_only=True)

    def get_like_count(self, obj):
        return obj.likes.count()
    
    def get_is_edited(self, obj):
        return obj.histories.exists()

    class Meta:
        model = Review
        fields = ['id', 'user', 'movie', 'rating', 'comment', 'is_spoiler', 'created_at', 'like_count', 'is_edited', 'images']
        read_only_fields = ['user', 'created_at', 'like_count', 'is_edited']


# ✅ 리뷰 좋아요 Serializer: 내부 처리용 (Swagger에 직접 노출되진 않음)
class ReviewLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewLike
        fields = ['id', 'user', 'review', 'created_at']


# ✅ 리뷰 댓글 Serializer
class ReviewCommentSerializer(serializers.ModelSerializer):
    # 작성자 username을 읽기 전용으로 제공
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = ReviewComment
        fields = ['id', 'user', 'review', 'content', 'created_at']

        # 사용자가 직접 입력하지 않도록 처리
        read_only_fields = ['user', 'review', 'created_at']

class ReviewCommentReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewCommentReaction
        fields = ['id', 'user', 'comment', 'created_at']
        read_only_fields = ['id', 'user', 'created_at']

class ReviewReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewReaction
        fields = ['id', 'user', 'review', 'is_like', 'created_at']
        read_only_fields = ['id', 'user', 'created_at']

class ReviewHistorySerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = ReviewHistory
        fields = ['id', 'user', 'previous_rating', 'previous_comment', 'edited_at']
