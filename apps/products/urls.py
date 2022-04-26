from django.urls import path
from .views import *

urlpatterns = [
    path('category/<str:category_name>/', category, name="category"),
    path('product-listings/', product_listings, name="product_listings"),
    path('product-listing/<int:listing_id>/', product_listing, name="product_listing"),
]

