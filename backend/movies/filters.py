from django_filters.rest_framework import FilterSet, ModelMultipleChoiceFilter
from .models import Movie
from ott.models import OTT

class MovieFilter(FilterSet):
    ott_services = ModelMultipleChoiceFilter(
        field_name='ott_services',
        queryset=OTT.objects.all()
    )

    class Meta:
        model = Movie
        fields = ['ott_services']