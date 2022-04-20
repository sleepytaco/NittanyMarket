from django.urls import path
from .views import *

urlpatterns = [
    path('category/<str:category_name>/', category, name="category"),
    path('product-listings/', product_listings, name="product_listings"),
]

