from django.core.management.base import BaseCommand
from events.models import Event, Category
from django.contrib.auth import get_user_model
from datetime import date, timedelta
import random

User = get_user_model()

class Command(BaseCommand):
    help = "Create 10 dummy events for the first user"

    def handle(self, *args, **options):
        user = User.objects.first()
        if not user:
            self.stdout.write(self.style.ERROR("No users in DB. Create a superuser first."))
            return
        cat, _ = Category.objects.get_or_create(name='Sample', defaults={'color':'#ff8800'})
        for i in range(10):
            Event.objects.create(
                title = f"Demo Event {i+1}",
                description = "Auto-generated event",
                date = date.today() + timedelta(days=random.randint(1,30)),
                category = cat,
                user = user
            )
        self.stdout.write(self.style.SUCCESS("10 dummy events created"))
