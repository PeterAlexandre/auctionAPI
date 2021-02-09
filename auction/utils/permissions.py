from rest_framework.permissions import BasePermission


class IsStaff(BasePermission):
    def has_permission(self, request, view) -> bool:
        return request.user.is_staff


class IsSelfUserOrIsStaff(BasePermission):
    def check_object_permission(self, user, obj):
        return (user.is_staff or obj == user)

    def has_object_permission(self, request, view, obj):
        return self.check_object_permission(request.user, obj)


class IsOwnerOrIsStaff(BasePermission):
    def check_object_permission(self, user, obj):
        return (user.is_staff or obj.owner == user)

    def has_object_permission(self, request, view, obj):
        return self.check_object_permission(request.user, obj)
