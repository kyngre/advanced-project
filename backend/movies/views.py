from rest_framework import generics, filters
from .models import Movie
from .serializers import MovieSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated

class MovieListView(generics.ListAPIView):
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['average_rating', 'release_date', 'title']
    ordering = ['-average_rating']

    def get_queryset(self):
        return Movie.objects.prefetch_related('reviews', 'ott_services')

class MovieCreateView(generics.CreateAPIView):
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        movie = serializer.save()
        ott_ids = self.request.data.get('ott_services', [])
        movie.ott_services.set(ott_ids) 

class MovieDetailView(generics.RetrieveAPIView):
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Movie.objects.prefetch_related('reviews__user', 'ott_services')

class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]