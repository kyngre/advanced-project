from django.urls import path
from .views import OTTListView

urlpatterns = [
    # ✅ OTT 플랫폼 목록 조회
    # GET /api/ott/
    # 예: 넷플릭스, 디즈니+, 왓챠 등
    path('', OTTListView.as_view(), name='ott-list'),
]