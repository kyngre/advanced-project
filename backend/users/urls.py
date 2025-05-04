from django.urls import path
from .views import RegisterView, ProfileView, subscribe_ott

urlpatterns = [
    # ✅ 회원가입: POST 요청 (이메일, 사용자명, 비밀번호 입력)
    path('register/', RegisterView.as_view(), name='register'),

    # ✅ 사용자 프로필 조회: GET 요청 (로그인 필수)
    path('profile/', ProfileView.as_view(), name='profile'),

    # ✅ OTT 구독 설정: POST 요청 (로그인 필수, ott_ids 배열 입력)
    path('subscribe/', subscribe_ott, name='subscribe-ott'), 
]