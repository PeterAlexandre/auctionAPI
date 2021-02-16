from rest_framework.permissions import BasePermission


class IsSelfUserOrIsStaff(BasePermission):
    def check_object_permission(self, user, obj):
        return (user.is_staff or obj == user)

    def has_object_permission(self, request, view, obj):
        return self.check_object_permission(request.user, obj)


class IsOwnerOrIsStaff(BasePermission):
    def check_object_permission(self, user, obj):
        return (user.is_staff or obj.user == user)

    def has_object_permission(self, request, view, obj):
        return self.check_object_permission(request.user, obj)
