import django.contrib.auth.models as django_auth_models
from django.db import models
from django.db.models import ImageField


class User(django_auth_models.AbstractUser):
    profile_picture = ImageField()
