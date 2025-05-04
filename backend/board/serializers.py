from rest_framework import serializers
from .models import BoardPost, BoardComment

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