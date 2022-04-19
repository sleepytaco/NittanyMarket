from django.contrib import admin
from .models import *
from django.contrib.auth.models import User

admin.site.unregister(User)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'password')


@admin.register(ZipcodeInfo)
class ZipcodeInfoAdmin(admin.ModelAdmin):
    list_display = ('zipcode', 'city', 'state_id', 'population', 'density', 'county_name', 'timezone')


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('address_id', 'zipcode', 'street_num', 'street_name')


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('buyer_email', 'first_name', 'last_name', 'gender', 'age', 'home_address_id', 'billing_address_id')


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('seller_email', 'routing_number', 'account_number', 'balance')


@admin.register(LocalVendor)
class LocalVendorAdmin(admin.ModelAdmin):
    list_display = ('vendor_email', 'business_name', 'business_address_id', 'customer_service_num')
