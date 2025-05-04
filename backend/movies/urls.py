from django.urls import path
from .views import MovieListView, MovieCreateView, MovieDetailView

urlpatterns = [
    # ✅ 영화 목록 조회
    # GET /api/movies/
    # 정렬 가능: ?ordering=average_rating / release_date / title
    path('', MovieListView.as_view(), name='movie-list'),

    # ✅ 영화 등록
    # POST /api/movies/create/
    # 인증된 사용자만 사용 가능 (OTT 연결 포함)
    path('create/', MovieCreateView.as_view(), name='movie-create'),

    # ✅ 영화 상세 조회 / 수정 / 삭제
    # GET / PUT / DELETE /api/movies/<pk>/
    path('<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
]