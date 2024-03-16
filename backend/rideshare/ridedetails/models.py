from django.db import models

class Ride(models.Model):
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    estimatedAmount = models.CharField(max_length=100)
    date = models.DateField()
    # Add more fields as needed