from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView, \
    PasswordResetView, PasswordChangeView, PasswordChangeDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView
from django.views.generic.edit import CreateView
from .forms import UserRegistrationForm

class UserRegistrationView(CreateView):
    form_class = UserRegistrationForm
    model = get_user_model()
    template_name = "users/register.html"
    success_url = ""

class UserLoginView(LoginView):
    template_name = "users/login.html"
    success_url = ""

class UserLogoutView(LogoutView):
    template_name = "users/logout.html"

class UserPasswordResetView(PasswordResetView):
    template_name = "users/password_reset.html"

class UserPasswordChangeView(PasswordChangeView):
    template_name = "users/password_change.html"

class UserPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = "users/password_change_done.html"

class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = "users/password_reset_confirm.html"

class UserPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = "users/password_reset_complete.html"