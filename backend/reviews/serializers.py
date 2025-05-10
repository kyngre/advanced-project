from rest_framework import serializers
from .models import (
    Review, ReviewHistory, ReviewImage, ReviewLike,
    ReviewComment, ReviewReaction, ReviewCommentReaction
)

# ---------------------------------------------------------------------
# ✅ 리뷰 이미지 Serializer (이미지 업로드용)
# ---------------------------------------------------------------------
class ReviewImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewImage
        fields = ['id', 'image', 'uploaded_at']
        read_only_fields = ['id', 'uploaded_at']

# ---------------------------------------------------------------------
# ✅ 리뷰 Serializer: 평점, 코멘트, 스포일러, 이미지 등 포함
# ---------------------------------------------------------------------
class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    rating = serializers.IntegerField(min_value=1, max_value=5)
    is_spoiler = serializers.BooleanField(default=False)
    like_count = serializers.SerializerMethodField()
    is_edited = serializers.SerializerMethodField()
    images = ReviewImageSerializer(many=True, read_only=True)

    def get_like_count(self, obj):
        return obj.likes.count()

    def get_is_edited(self, obj):
        return obj.histories.exists()

    class Meta:
        model = Review
        fields = [
            'id', 'user', 'movie', 'rating', 'comment', 'is_spoiler',
            'created_at', 'like_count', 'is_edited', 'images'
        ]
        read_only_fields = ['user', 'created_at', 'like_count', 'is_edited']

# ---------------------------------------------------------------------
# ✅ 리뷰 좋아요 Serializer (내부 로직 처리용)
# ---------------------------------------------------------------------
class ReviewLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewLike
        fields = ['id', 'user', 'review', 'created_at']

# ---------------------------------------------------------------------
# ✅ 리뷰 댓글 Serializer
# ---------------------------------------------------------------------
class ReviewCommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = ReviewComment
        fields = ['id', 'user', 'review', 'content', 'created_at']
        read_only_fields = ['user', 'review', 'created_at']

# ---------------------------------------------------------------------
# ✅ 댓글 좋아요 Serializer
# ---------------------------------------------------------------------
class ReviewCommentReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewCommentReaction
        fields = ['id', 'user', 'comment', 'created_at']
        read_only_fields = ['id', 'user', 'created_at']

# ---------------------------------------------------------------------
# ✅ 리뷰 추천/비추천 Serializer
# ---------------------------------------------------------------------
class ReviewReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewReaction
        fields = ['id', 'user', 'review', 'is_like', 'created_at']
        read_only_fields = ['id', 'user', 'created_at']

# ---------------------------------------------------------------------
# ✅ 리뷰 수정 이력 Serializer
# ---------------------------------------------------------------------
class ReviewHistorySerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = ReviewHistory
        fields = ['id', 'user', 'previous_rating', 'previous_comment', 'edited_at']