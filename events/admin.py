from django.contrib import admin
from .models import Category, Event, Location, Tag, Reminder

admin.site.register(Category)
admin.site.register(Event)
admin.site.register(Location)
admin.site.register(Tag)
admin.site.register(Reminder)
