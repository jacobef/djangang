from django.contrib import admin
from mapbox_location_field.admin import MapAdmin

from rental.models import Tool

admin.site.register(Tool, MapAdmin)
