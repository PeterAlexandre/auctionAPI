from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from auction.users.views import UserViewSet, AddressViewSet
from auction.core.views import AuctionViewSet

# trailing_slash=False: should not contain "/" at the end of the url
router = routers.DefaultRouter(trailing_slash=False)
router.register(r"users", UserViewSet)
router.register(r"address", AddressViewSet)
router.register(r"auction", AuctionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(router.urls)),
]
