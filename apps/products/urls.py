from django.urls import path
from .views import *

urlpatterns = [
    path('category/<str:category_name>', category, name="category"),
]

