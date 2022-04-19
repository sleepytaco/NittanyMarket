from django.contrib import admin
from .models import *


@admin.register(CreditCard)
class CreditCardAdmin(admin.ModelAdmin):
    list_display = ('card_num', 'card_code', 'expire_month', 'expire_year', 'card_type', 'owner')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'seller', 'listing_id', 'buyer', 'date', 'quantity', 'payment')
