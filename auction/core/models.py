from django.conf import settings
from django.db import models

from auction.core import choices


class Auction(models.Model):
    STATUS = choices.AuctionStatus

    title = models.CharField(max_length=60)
    description = models.TextField(blank=True)
    deadline = models.DateTimeField()
    status = models.CharField(max_length=1, choices=STATUS.choices, default="O")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="auctions",
        related_query_name="auction",
    )

    class Meta:
        ordering = ["pk"]

    def __str__(self):
        return self.title


class Item(models.Model):
    STATUS = choices.ItemStatus

    title = models.CharField(max_length=60)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=1, choices=STATUS.choices, default="U")
    status = models.DecimalField(max_digits=12, decimal_places=2)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name='items', related_query_name='item')

    class Meta:
        ordering = ["pk"]

    def __str__(self):
        return self.title


class Bid(models.Model):
    price = models.DecimalField(max_digits=12, decimal_places=2)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='Bids', related_query_name='Bid')
    Buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
