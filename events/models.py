from django.db import models
from django.conf import settings
class Category(models.Model):
    name = models.CharField(max_length=100)    
    color = models.CharField(max_length=7, default="#3366cc")  # store hex color like #ff0000

    def __str__(self):
        return self.name

class Event(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return f"{self.title} ({self.date})"

class Location(models.Model):
    name = models.CharField(max_length=150)
    events = models.ManyToManyField(Event, related_name='locations', blank=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)
    events = models.ManyToManyField(Event, related_name='tags', blank=True)

    def __str__(self):
        return self.name

class Reminder(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    message = models.CharField(max_length=200)

    def __str__(self):
        return f"Reminder for {self.event.title}"
