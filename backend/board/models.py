from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# ✅ 게시글 모델
class BoardPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="작성자")
    title = models.CharField(max_length=200, verbose_name="제목")
    content = models.TextField(verbose_name="내용")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# ✅ 댓글 모델
class BoardComment(models.Model):
    post = models.ForeignKey(BoardPost, on_delete=models.CASCADE, related_name='comments', verbose_name="게시글")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="작성자")
    content = models.TextField(verbose_name="댓글 내용")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.content[:20]}"