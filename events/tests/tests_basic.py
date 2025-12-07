import pytest
from django.contrib.auth import get_user_model
from events.models import Category, Event
from datetime import date

User = get_user_model()

@pytest.mark.django_db
def test_create_event():
    user = User.objects.create_user(email="a@b.com", username="testuser", password="1234")
    cat = Category.objects.create(name="Test", color="#123456")
    e = Event.objects.create(user=user, title="E1", date=date.today(), description="desc", category=cat)
    assert e.title == "E1"
