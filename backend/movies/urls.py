from django.urls import path
from .views import MovieListView, MovieCreateView, MovieDetailView

urlpatterns = [
    path('', MovieListView.as_view(), name='movie-list'),  # GET
    path('create/', MovieCreateView.as_view(), name='movie-create'),  # POST
    path('<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),  # GET /1/
]