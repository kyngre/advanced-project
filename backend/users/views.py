from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .serializers import RegisterSerializer
from ott.models import OTT

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


# ✅ 회원가입 API
class RegisterView(APIView):
    @swagger_auto_schema(
        operation_summary="회원가입",
        operation_description="email, username, password를 입력하여 회원가입을 진행합니다.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["email", "username", "password"],
            properties={
                "email": openapi.Schema(type=openapi.TYPE_STRING, format="email", description="이메일"),
                "username": openapi.Schema(type=openapi.TYPE_STRING, description="사용자명"),
                "password": openapi.Schema(type=openapi.TYPE_STRING, format="password", description="비밀번호"),
            },
        ),
        responses={201: openapi.Response(description="회원가입 성공")},
    )
    def post(self, request):
        """
        POST /api/users/register/
        새로운 사용자를 생성합니다.
        """
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "회원가입 성공!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ✅ 사용자 프로필 조회 API (로그인 필요)
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="프로필 조회",
        operation_description="로그인한 사용자의 이메일과 사용자명을 반환합니다.",
        responses={200: openapi.Response(
            description="사용자 프로필 정보",
            examples={
                "application/json": {
                    "email": "example@example.com",
                    "username": "exampleuser"
                }
            }
        )}
    )
    def get(self, request):
        """
        GET /api/users/profile/
        로그인한 사용자의 정보를 반환합니다.
        """
        user = request.user
        return Response({
            "email": user.email,
            "username": user.username,
        })


# ✅ OTT 구독 설정 API (로그인 필요)
@swagger_auto_schema(
    method='post',
    operation_summary="OTT 구독 설정",
    operation_description="사용자가 구독할 OTT 플랫폼 목록을 설정합니다.",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['ott_ids'],
        properties={
            'ott_ids': openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Items(type=openapi.TYPE_INTEGER),
                description='구독할 OTT ID 배열 (예: [1, 2])'
            )
        }
    ),
    responses={200: openapi.Response(
        description="구독 정보가 갱신되었습니다.",
        examples={"application/json": {"message": "구독 정보가 갱신되었습니다."}}
    )}
)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def subscribe_ott(request):
    """
    POST /api/users/subscribe/
    사용자에게 OTT 구독 정보를 설정합니다.
    """
    ott_ids = request.data.get('ott_ids', [])
    if not isinstance(ott_ids, list):
        return Response({'error': 'ott_ids는 리스트여야 합니다.'}, status=400)

    user = request.user
    user.subscribed_ott.set(ott_ids)
    return Response({'message': '구독 정보가 갱신되었습니다.'})