from django.contrib import admin

from auction.core.models import Auction, Item, Bid

admin.site.register(Auction)
admin.site.register(Item)
admin.site.register(Bid)
