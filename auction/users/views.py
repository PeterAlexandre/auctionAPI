from rest_framework.decorators import action
from rest_framework.response import Response

from auction.utils.views import MixedPermissionModelViewSet
from auction.utils.permissions import IsStaff, IsSelfUserOrIsStaff

from .models import User, Address
from .serializers import UserSerializer, ChangePasswordSerializer, AddressSerializer


class UserViewSet(MixedPermissionModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # add filterset fields

    permission_classes_by_action = {
        "list": [IsStaff],
        "retrieve": [IsSelfUserOrIsStaff],
        "create": [IsStaff],
        "update": [IsSelfUserOrIsStaff],
        "partial_update": [IsSelfUserOrIsStaff],
        "destroy": [IsSelfUserOrIsStaff],
    }

    @action(methods=["PATCH"], detail=True, permission_classes=[IsSelfUserOrIsStaff])
    def change_password(self, request, pk=None):
        user = self.get_object()
        serializer = ChangePasswordSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        user.set_password(serializer.validated_data.get("new_password"))
        user.save()

        return Response({"message": f"The {user.username}'s password was changed!"})

    @action(methods=["PATCH"], detail=True, permission_classes=[IsStaff])
    def change_permission(self, request, pk=None):
        instance = self.get_object()
        instance.is_staff = not instance.is_staff
        instance.save()

        return Response({"message": f"{instance.username}'s permission has been changed"})


class AddressViewSet(MixedPermissionModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    # add filterset fields

    permission_classes_by_action = {
        "list": [IsStaff],
        "retrieve": [IsStaff],
        "create": [IsStaff],
        "update": [IsSelfUserOrIsStaff],
        "partial_update": [IsSelfUserOrIsStaff],
        "destroy": [IsSelfUserOrIsStaff],
    }
