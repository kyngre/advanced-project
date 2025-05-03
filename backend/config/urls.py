from django.contrib import admin
from rest_framework import permissions
from django.urls import path, include
# Swagger 관련 import
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Swagger 스키마 설정
schema_view = get_schema_view(
    openapi.Info(
        title="Movie Review API",
        default_version='v1',
        description="영화 리뷰 사이트 API 문서입니다.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="youremail@example.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=(JWTAuthentication,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # 앱 없이 swagger만 보여주기
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/users/', include('users.urls')),  # 기존 회원가입 경로
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # 로그인
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # 리프레시
]