from rest_framework import generics
from .models import OTT
from .serializers import OTTSerializer

class OTTListView(generics.ListAPIView):
    queryset = OTT.objects.all()
    serializer_class = OTTSerializer