from django.contrib import messages
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST


def index(request):
    return render(request, 'users/index.html')


@login_required
def home(request):
    return render(request, 'users/home.html')


@require_POST
def sign_in(request):
    """
    This view is responsible to login users to the NittanyMarket portal.
    Referred to Django documentation to complete this function:
    https://docs.djangoproject.com/en/4.0/topics/auth/default/
    """
    email = request.POST["email"]
    password = request.POST["password"]
    user = authenticate(username=email, password=password)
    if user is not None:
        login(request, user)
        messages.success(request, "Successfully logged in!")
        return redirect('home')
    messages.error(request, "There was an error logging you in. Please confirm your email or password!")
    return redirect('index')


@login_required
def checking_info(request):
    if request.method == "POST":
        pass

    return render(request, "users/checking-info.html")


@login_required
@require_POST
def change_password(request):
    user = request.user
    if request.POST["new_password"] == '':
        messages.warning(request, "Enter a new password to change your current one!")
        return redirect('checking_info')

    if check_password(request.POST["current_password"], user.password):
        user.password = make_password(request.POST["new_password"])
        user.save(update_fields=['password'])
        update_session_auth_hash(request, user)  # updates the current session, so that user does not need to log back in
        messages.success(request, "Successfully updated your password!")
    else:
        messages.error(request, "You entered an incorrect current password. Please try again!")

    return redirect('checking_info')


@login_required
def sign_out(request):
    logout(request)
    messages.success(request, "Successfully logged out!")
    return redirect('index')
