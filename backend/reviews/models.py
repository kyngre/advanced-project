from django.db import models
from django.contrib.auth import get_user_model
from movies.models import Movie, Avg  # 영화 모델과 평균 집계 함수

User = get_user_model()


# ✅ 리뷰 모델
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 작성자
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')  # 리뷰 대상 영화
    rating = models.IntegerField()  # 평점 (1~5 사이 권장)
    comment = models.TextField(blank=True)  # 선택적 코멘트
    created_at = models.DateTimeField(auto_now_add=True)  # 생성 일시

    def save(self, *args, **kwargs):
        """
        저장 시 해당 영화의 평균 평점을 자동으로 갱신
        """
        super().save(*args, **kwargs)
        self.movie.average_rating = self.movie.reviews.aggregate(avg=Avg('rating'))['avg'] or 0
        self.movie.save()

    def delete(self, *args, **kwargs):
        """
        삭제 시에도 영화의 평균 평점을 갱신
        """
        movie = self.movie
        super().delete(*args, **kwargs)
        movie.average_rating = movie.reviews.aggregate(avg=Avg('rating'))['avg'] or 0
        movie.save()

    def __str__(self):
        return f"{self.user.username} - {self.movie.title} ({self.rating}점)"


# ✅ 리뷰 좋아요 모델
class ReviewLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 좋아요 누른 사용자
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='likes')  # 좋아요 대상 리뷰
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'review')  # 한 사용자가 같은 리뷰에 여러 번 좋아요 못 누르게 제한

    def __str__(self):
        return f"{self.user.username} ❤️ {self.review}"


# ✅ 리뷰 댓글 모델
class ReviewComment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments')  # 댓글 단 대상 리뷰
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 댓글 작성자
    content = models.TextField()  # 댓글 내용
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.content[:20]}"