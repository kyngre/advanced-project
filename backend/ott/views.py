from rest_framework import generics
from .models import OTT
from .serializers import OTTSerializer

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


# ✅ OTT 플랫폼 목록 조회 API
class OTTListView(generics.ListAPIView):
    """
    GET /api/ott/
    전체 OTT 플랫폼 목록을 조회합니다.
    예: 넷플릭스, 디즈니+, 왓챠 등
    """
    queryset = OTT.objects.all()
    serializer_class = OTTSerializer

    @swagger_auto_schema(
        operation_summary="OTT 플랫폼 목록 조회",
        operation_description="등록된 OTT 플랫폼 리스트를 반환합니다.",
        responses={200: OTTSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)