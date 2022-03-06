from accounts.models import User
from django.db import models
from django.db.models import DecimalField
from mapbox_location_field.models import LocationField


class Tool(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    location = LocationField()
    brand = models.CharField(max_length=50)
    description = models.TextField(max_length=5000)
    price = DecimalField(decimal_places=2, max_digits=7)

    class Type(models.TextChoices):
        IMPACT_DRIVER = 'Impact Driver'
        WIZARDING_WAND = 'Wizarding Wand'
        OTHER = 'Other'
    type = models.CharField(choices=Type.choices, max_length=50)

