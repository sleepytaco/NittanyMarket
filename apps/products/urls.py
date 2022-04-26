from django.urls import path
from .views import *

urlpatterns = [
    path('category/<str:category_name>/', category, name="category"),
    path('create/product-listing/', create_product_listing, name="create_product_listing"),
    path('remove/product-listing/<int:listing_id>/', remove_product_listing, name="remove_product_listing"),
    path('product-listings/', product_listings, name="product_listings"),
    path('product-listing/<int:listing_id>/', product_listing, name="product_listing"),
    path('search/', search, name="search"),
]

