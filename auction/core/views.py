from rest_framework.permissions import IsAuthenticated

from auction.utils.views import MixedPermissionModelViewSet
from auction.utils.permissions import IsOwnerOrIsStaff

from .models import Auction, Item, Bid
from .serializers import AuctionSerializer, ItemSerializer, BidSerializer

# auction slug_field deve ser "url" se a requisição for "GET"


class AuctionViewSet(MixedPermissionModelViewSet):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer
    # add filterset fields

    permission_classes_by_action = {
        "list": [],
        "retrieve": [],
        "create": [IsAuthenticated],
        "update": [IsOwnerOrIsStaff],
        "partial_update": [IsOwnerOrIsStaff],
        "destroy": [IsOwnerOrIsStaff],
    }

    def perform_destroy(self, instance):
        """Soft delete."""
        instance.status = "C"
        instance.save()
