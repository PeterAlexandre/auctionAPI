from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Auction, Item, Bid

USER_MODEL = get_user_model()


class AuctionSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field="username",
        queryset=USER_MODEL.objects.all()
    )

    class Meta:
        model = Auction
        fields = [
            "url",
            "id",
            "title",
            "description",
            "deadline",
            "status",
            "user",
        ]


class ItemSerializer(serializers.ModelSerializer):
    auction = serializers.SlugRelatedField(
        slug_field="pk",
        queryset=Auction.objects.all()
    )

    class Meta:
        model = Item
        fields = [
            "url",
            "id",
            "title",
            "description",
            "status",
            "status",
            "auction",
        ]


class BidSerializer(serializers.ModelSerializer):
    item = ItemSerializer()
    Buyer = serializers.SlugRelatedField(
        slug_field="username",
        queryset=USER_MODEL.objects.all()
    )

    class Meta:
        model = Bid
        fields = [
            "url",
            "id",
            "price",
            "item",
            "buyer"
        ]
