from rest_framework import generics
from .models import Movie
from .serializers import MovieSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class MovieListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        movie = serializer.save()
        ott_ids = self.request.data.get('ott_services', [])
        movie.ott_services.set(ott_ids)  # M2M 필드 설정

class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]