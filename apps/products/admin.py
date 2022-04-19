from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('parent_category', 'category_name')


@admin.register(ProductListing)
class ProductListingAdmin(admin.ModelAdmin):
    list_display = ('seller', 'listing_id', 'category', 'title', 'product_name', 'product_description', 'price', 'quantity')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('buyer', 'seller', 'listing_id', 'review_desc')


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('buyer', 'seller', 'date', 'rating', 'rating_desc')

