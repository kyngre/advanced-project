from django.urls import path
from .views import (
    MovieListView,
    MovieCreateView,
    MovieDetailView,
    MovieDetailEditDeleteView,
    MovieSearchView,
)

urlpatterns = [
    # 🎬 영화 목록 조회 (정렬 가능)
    # GET /api/movies/?ordering=average_rating|release_date|title
    path('', MovieListView.as_view(), name='movie-list'),

    # 🎬 영화 등록 (인증 필요)
    # POST /api/movies/create/
    path('create/', MovieCreateView.as_view(), name='movie-create'),

    # 🎬 영화 상세 조회 (GET)
    # GET /api/movies/<int:pk>/
    path('<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),

    # 🎬 영화 수정 / 삭제 (PUT, DELETE)
    # PUT / DELETE /api/movies/<int:pk>/
    path('<int:pk>/edit/', MovieDetailEditDeleteView.as_view(), name='movie-edit-delete'),

    # 🎬 영화 검색 + OTT 필터
    # GET /api/movies/search/?search=제목키워드&ott_services=1,2
    path('search/', MovieSearchView.as_view(), name='movie-search'),
]