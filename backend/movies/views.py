from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import Movie
from .serializers import MovieSerializer

from .filters import MovieFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView


# ✅ 영화 목록 조회 API (정렬 포함)
class MovieListView(generics.ListAPIView):
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.OrderingFilter]  # 정렬 기능 추가
    ordering_fields = ['average_rating', 'release_date', 'title']  # 정렬 가능한 필드 목록
    ordering = ['-average_rating']  # 기본 정렬: 평점 내림차순

    @swagger_auto_schema(
        operation_summary="영화 목록 조회",
        operation_description="등록된 영화들의 목록을 조회합니다. 평균 평점, 출시일, 제목으로 정렬할 수 있습니다.\n\n예: `/api/movies/?ordering=-average_rating`",
        manual_parameters=[
            openapi.Parameter(
                'ordering',
                openapi.IN_QUERY,
                description="정렬 기준 (`average_rating`, `release_date`, `title`)",
                type=openapi.TYPE_STRING
            )
        ],
        responses={200: MovieSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        # 리뷰와 ott_services를 사전 로딩하여 쿼리 최적화 (N+1 문제 해결)
        return Movie.objects.prefetch_related('reviews', 'ott_services')


# ✅ 영화 생성 API (관리자/사용자 권한 필요)
class MovieCreateView(generics.CreateAPIView):
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="영화 생성",
        operation_description="새로운 영화를 등록합니다. `ott_services` 필드에는 등록할 OTT ID 리스트를 입력하세요.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["title", "description", "release_date", "thumbnail_url", "ott_services"],
            properties={
                "title": openapi.Schema(type=openapi.TYPE_STRING, description="영화 제목"),
                "description": openapi.Schema(type=openapi.TYPE_STRING, description="영화 설명"),
                "release_date": openapi.Schema(type=openapi.TYPE_STRING, format="date", description="출시일"),
                "thumbnail_url": openapi.Schema(type=openapi.TYPE_STRING, format="uri", description="썸네일 이미지 URL"),
                "ott_services": openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Items(type=openapi.TYPE_INTEGER),
                    description="연결할 OTT ID 배열 (예: [1,2])"
                ),
            }
        ),
        responses={201: MovieSerializer}
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def perform_create(self, serializer):
        # 영화 저장 후 ManyToMany 필드인 ott_services 따로 연결
        movie = serializer.save()
        ott_ids = self.request.data.get('ott_services', [])
        movie.ott_services.set(ott_ids)


# ✅ 영화 상세 조회 API
class MovieDetailView(generics.RetrieveAPIView):
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(
        operation_summary="영화 상세 조회",
        operation_description="특정 영화의 상세 정보를 조회합니다. 리뷰 목록과 평균 평점 포함됩니다.",
        responses={200: MovieSerializer}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        # 리뷰와 작성자, ott를 미리 불러와 쿼리 최적화
        return Movie.objects.prefetch_related('reviews__user', 'ott_services')


# ✅ 영화 수정/삭제 API (작성자 권한 필요 시 수정 가능)
class MovieDetailEditDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(operation_summary="영화 상세 조회")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="영화 정보 수정",
        request_body=MovieSerializer,
        responses={200: MovieSerializer}
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="영화 삭제")
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    
class MovieSearchView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['title']
    filterset_class = MovieFilter