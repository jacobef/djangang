import django.contrib.auth.views as django_auth_views
from accounts import views
from django.urls import path
app_name = "accounts"


urlpatterns = [
    path('login/', views.LoginView.as_view(), name="login"),
    path('register/', views.UserCreateView.as_view(), name="register"),
    path('profile/', views.profile, name="profile"),
]
