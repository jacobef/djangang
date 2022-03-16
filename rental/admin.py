from django.contrib import admin
from mapbox_location_field.admin import MapAdmin

from rental.models import Tool, RentalRequest

admin.site.register(Tool, MapAdmin)
admin.site.register(RentalRequest)
