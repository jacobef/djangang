from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
import django.contrib.auth.views as django_auth_views
# Create your views here.
from django.views.generic import CreateView


def splash(request):
    return render(request, "accounts/splash.html")


class UserCreateView(CreateView):
    template_name = "accounts/register.html"
    form_class = UserCreationForm
    success_url = "/accounts/login"


def my_account(request):
    return render(request, "accounts/my_account.html")


class LoginView(django_auth_views.LoginView):
    template_name = "accounts/login.html"
