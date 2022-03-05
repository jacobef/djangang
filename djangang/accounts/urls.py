import django.contrib.auth.views as django_auth_views
from accounts import views
from django.urls import path

urlpatterns = [
    path('login/', views.LoginView.as_view()),
]