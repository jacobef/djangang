import django.contrib.auth as django_auth
from django.urls import path

urlpatterns = [
    path('login/', django_auth.login),
]