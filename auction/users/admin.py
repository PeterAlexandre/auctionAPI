from django.contrib import admin

from auction.users.models import User, Address

admin.site.register(User)
admin.site.register(Address)
