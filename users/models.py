from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Make email required and unique
    email = models.EmailField(unique=True)

    # Use email as username field
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # username still required by AbstractUser 
