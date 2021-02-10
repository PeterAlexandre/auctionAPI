from rest_framework.decorators import action
from rest_framework.response import Response

from auction.utils.views import MixedPermissionModelViewSet
from auction.utils.permissions import IsStaff, IsSelfUserOrIsStaff, IsOwnerOrIsStaff

from .models import User, Address
from .serializers import UserSerializer, PublicUserSerializer, ChangePasswordSerializer, AddressSerializer


class UserViewSet(MixedPermissionModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # add filterset fields

    permission_classes_by_action = {
        "list": [],
        "retrieve": [IsSelfUserOrIsStaff],
        "create": [IsStaff],
        "update": [IsSelfUserOrIsStaff],
        "partial_update": [IsSelfUserOrIsStaff],
        "destroy": [IsSelfUserOrIsStaff],
    }

    def get_serializer_class(self):
        if self.action == "list" and not self.request.user.is_staff:
            # raise Exception(PublicUserSerializer.Meta.fields)
            self.serializer_class = PublicUserSerializer

        return self.serializer_class

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
        "retrieve": [IsOwnerOrIsStaff],
        "create": [IsStaff],
        "update": [IsSelfUserOrIsStaff],
        "partial_update": [IsSelfUserOrIsStaff],
        "destroy": [IsSelfUserOrIsStaff],
    }
