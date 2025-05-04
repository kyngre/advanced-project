from rest_framework import serializers
from .models import BoardPost, BoardComment, BoardPostLike, BoardCommentLike

# ✅ 게시글 직렬화기
class BoardPostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')  # 작성자 표시 (읽기 전용)

    class Meta:
        model = BoardPost
        fields = ['id', 'user', 'title', 'content', 'created_at']


# ✅ 댓글 직렬화기
class BoardCommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')  # 작성자 표시 (읽기 전용)

    class Meta:
        model = BoardComment
        fields = ['id', 'post', 'user', 'content', 'created_at']
        read_only_fields = ['user', 'post', 'created_at']


class BoardPostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardPostLike
        fields = ['id', 'user', 'post', 'is_like', 'created_at']
        read_only_fields = ['user']

class BoardCommentLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardCommentLike
        fields = ['id', 'user', 'comment', 'is_like', 'created_at']
        read_only_fields = ['user']