from django.db import models
from ott.models import OTT
from django.db.models import Avg

# ✅ 영화 모델 정의
class Movie(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="영화 제목",
        help_text="영화의 제목입니다."
    )
    description = models.TextField(
        verbose_name="영화 설명",
        help_text="영화의 줄거리 또는 개요를 입력합니다."
    )
    release_date = models.DateField(
        verbose_name="개봉일",
        help_text="영화의 공식 개봉일입니다."
    )
    thumbnail_url = models.URLField(
        blank=True,
        null=True,
        verbose_name="썸네일 이미지",
        help_text="포스터나 썸네일 이미지의 URL입니다. (선택사항)"
    )

    # ✅ 영화가 제공되는 OTT 플랫폼 (다대다 관계)
    ott_services = models.ManyToManyField(
        OTT,
        related_name='movies',
        verbose_name="제공 OTT"
    )

    # ✅ 저장된 평균 평점 필드 (API 정렬용 캐싱)
    average_rating_cache = models.FloatField(
        default=0.0,
        verbose_name="평점 평균 캐시",
        help_text="DB에 저장된 평균 평점 (성능 개선용)"
    )

    def calculate_average_rating(self):
        """
        연결된 리뷰의 평균 평점을 계산하여 반환합니다.
        (reviews는 related_name으로 연결되어 있어야 함)
        """
        return self.reviews.aggregate(avg=Avg('rating'))['avg'] or 0

    def __str__(self):
        return self.title