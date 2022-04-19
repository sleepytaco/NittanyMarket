from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('portal/', home, name="home"),
    path('checking-info/', checking_info, name="checking_info"),
    path('change-password/', change_password, name="change_password"),
    path('sign-in/', sign_in, name="sign_in"),
    path('sign-out/', sign_out, name="sign_out"),
]

