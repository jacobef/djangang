import django.contrib.auth.forms as django_auth_forms
import django.contrib.auth.views as django_auth_views
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from accounts import models


def splash(request):
    return render(request, "accounts/splash.html")


class UserCreationForm(django_auth_forms.UserCreationForm):
    class Meta:
        model = models.User
        fields = "__all__"


class UserCreateView(CreateView):
    template_name = "accounts/register.html"
    form_class = UserCreationForm
    success_url = "/accounts/login"


@method_decorator(login_required, name='dispatch')
class Profile(UpdateView):
    model = models.User
    template_name = "accounts/profile.html"
    fields = ["username", "first_name", "last_name", "email", "profile_picture"]
    success_url = reverse_lazy("accounts:profile")

    def get_object(self, queryset=None):
        return self.request.user


class LoginView(django_auth_views.LoginView):
    template_name = "accounts/login.html"
