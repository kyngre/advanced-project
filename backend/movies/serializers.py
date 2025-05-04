from rest_framework import serializers
from .models import Movie
from ott.models import OTT
from reviews.serializers import ReviewSerializer

class OTTSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTT
        fields = ['id', 'name', 'logo_url']
        ref_name = 'MovieApp_OTT'

class MovieSerializer(serializers.ModelSerializer):
    ott_services = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=OTT.objects.all()
    )
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'release_date', 'thumbnail_url', 'ott_services']