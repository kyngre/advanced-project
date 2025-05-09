from django.contrib import admin
from .models import Review, ReviewLike, ReviewComment

# ---------------------------------------------------------------------
# ✅ 리뷰 모델 관리자 설정
# ---------------------------------------------------------------------
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'movie', 'rating', 'created_at', 'is_spoiler')
    list_filter = ('movie', 'created_at', 'is_spoiler')
    search_fields = ('user__username', 'movie__title', 'comment')
    ordering = ('-created_at',)


# ---------------------------------------------------------------------
# ✅ 리뷰 좋아요 모델 관리자 설정
# ---------------------------------------------------------------------
@admin.register(ReviewLike)
class ReviewLikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'review', 'created_at')
    search_fields = ('user__username',)


# ---------------------------------------------------------------------
# ✅ 리뷰 댓글 모델 관리자 설정
# ---------------------------------------------------------------------
@admin.register(ReviewComment)
class ReviewCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'review', 'created_at', 'like_count')
    search_fields = ('user__username', 'content')
    ordering = ('-created_at',)