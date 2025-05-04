from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    커스텀 권한 클래스:
    - 읽기 요청(GET, HEAD, OPTIONS)은 누구나 허용
    - 수정/삭제 요청은 객체의 작성자만 허용
    """

    def has_object_permission(self, request, view, obj):
        # ✅ 읽기 권한은 항상 허용 (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True

        # ✅ 수정/삭제 권한은 객체 작성자에게만 허용
        return obj.user == request.user