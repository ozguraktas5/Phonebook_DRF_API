from rest_framework import permissions

class IsRequestUserPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(request.user.pk == obj.pk)