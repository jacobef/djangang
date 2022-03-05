from django.db import models
from mapbox_location_field.models import LocationField


class Tool(models.Model):
    location = LocationField()

# Create your models here.
