from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from events.models import Event, Category
from .models import CustomUser
from datetime import date, timedelta

@receiver(post_save, sender=CustomUser)
def welcome_and_sample(sender, instance, created, **kwargs):
    if created:
        # simple welcome print (in real app send email)
        print(f"Welcome {instance.email} — registration successful!")

        # create a default category if none exists
        cat, _ = Category.objects.get_or_create(name='General', defaults={'color':'#6c757d'})
        # create a sample event for the new user
        Event.objects.create(
            title='Welcome Event',
            description='This is a sample event created for you.',
            date = date.today() + timedelta(days=1),
            category = cat,
            user = instance
        )
