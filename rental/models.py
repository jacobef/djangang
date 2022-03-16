from accounts.models import User
from django.db import models
from django.db.models import DecimalField
from mapbox_location_field.models import LocationField


class Tool(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    location = LocationField(map_attrs={"zoom": 3, "center": [0,0], "marker_color": "lightblue", "style":"mapbox://styles/sast2883/cl0f8malf00vr16kdicnt4poy"})
    brand = models.CharField(max_length=50)
    description = models.TextField(max_length=5000)
    price = DecimalField(decimal_places=2, max_digits=7)

    class Type(models.TextChoices):
        IMPACT_DRIVER = 'Impact Driver'
        WIZARDING_WAND = 'Wizarding Wand'
        OTHER = 'Other'
    type = models.CharField(choices=Type.choices, max_length=50)


class RentalRequest(models.Model):
    tool = models.ForeignKey(to=Tool, on_delete=models.CASCADE)
    sender = models.ForeignKey(to=User, related_name="sender", on_delete=models.CASCADE)
    recipient = models.ForeignKey(to=User, related_name="recipient", on_delete=models.CASCADE)
    using_for = models.TextField(max_length=5000)
    approved = models.BooleanField(null=True)
    rejected = models.BooleanField(null=True)
    decision_message = models.TextField(max_length=5000, null=True)