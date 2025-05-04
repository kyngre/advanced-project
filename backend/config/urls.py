from django.contrib import admin
from django.urls import path, include

# REST framework 권한 설정
from rest_framework import permissions

# JWT 인증
from rest_framework_simplejwt.views import (
    TokenObtainPairView,   # 로그인 (Access + Refresh 토큰 발급)
    TokenRefreshView       # Refresh 토큰을 통한 Access 갱신
)
from rest_framework_simplejwt.authentication import JWTAuthentication

# ✅ Swagger / Redoc 문서 관련
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Swagger 스키마 정보 정의
schema_view = get_schema_view(
    openapi.Info(
        title="🎬 Movie Review API",
        default_version='v1',
        description="영화 리뷰 웹사이트의 Django REST API 문서입니다.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="youremail@example.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=(JWTAuthentication,),  # Swagger 내 인증 지원
)

urlpatterns = [
    # ✅ 관리자 페이지
    path('admin/', admin.site.urls),

    # ✅ Swagger 문서 UI
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # Swagger UI
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),            # ReDoc UI

    # ✅ JWT 인증 (로그인 및 토큰 갱신)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),      # 로그인
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),      # 토큰 재발급

    # ✅ 사용자 관련 API
    path('api/users/', include('users.urls')),

    # ✅ OTT 관련 API
    path('api/ott/', include('ott.urls')),

    # ✅ 영화 관련 API
    path('api/movies/', include('movies.urls')),

    # ✅ 리뷰 + 댓글 + 좋아요 API
    path('api/reviews/', include('reviews.urls')),
]