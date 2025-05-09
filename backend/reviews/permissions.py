from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    ✅ 객체 단위 커스텀 권한:
    - 안전한 요청(GET, HEAD, OPTIONS)은 모든 사용자에게 허용
    - 그 외 요청(PUT, DELETE 등)은 객체 작성자에게만 허용
    """

    def has_object_permission(self, request, view, obj):
        # 안전한 요청이면 항상 허용
        if request.method in permissions.SAFE_METHODS:
            return True

        # 요청자가 객체의 작성자인 경우에만 허용
        return obj.user == request.user