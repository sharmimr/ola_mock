from django.db import models
# from django.contrib.auth.models import AbstractUser

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    # Add other fields as needed

# class CustomUser(AbstractUser):
#     # Add custom fields here
#     pass