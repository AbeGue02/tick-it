from django.contrib import admin
from .models import Location, Venue, Event
# Register your models here.

admin.site.register(Location)
admin.site.register(Venue)
admin.site.register(Event)