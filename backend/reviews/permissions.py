from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    작성자만 수정/삭제 가능, 나머진 읽기만 가능
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True  # GET, HEAD, OPTIONS는 허용
        return obj.user == request.user  # 작성자만 수정/삭제 가능