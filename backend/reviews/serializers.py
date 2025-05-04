from rest_framework import serializers
from .models import Review, ReviewLike, ReviewComment

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    rating = serializers.IntegerField(min_value=1, max_value=5)
    like_count = serializers.SerializerMethodField()

    def get_like_count(self, obj):
        return obj.likes.count()

    class Meta:
        model = Review
        fields = ['id', 'user', 'movie', 'rating', 'comment', 'created_at', 'like_count']

class ReviewLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewLike
        fields = ['id', 'user', 'review', 'created_at']

class ReviewCommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = ReviewComment
        fields = ['id', 'user', 'review', 'content', 'created_at']
        read_only_fields = ['user', 'review', 'created_at']