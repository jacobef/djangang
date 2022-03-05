from django.shortcuts import render
import django.contrib.auth.views as django_auth_views
# Create your views here.


def splash(request):
    return render(request, "accounts/splash.html")


def my_account(request):
    return render(request, "accounts/my_account.html")


class LoginView(django_auth_views.LoginView):
    template_name = "accounts/login.html"
