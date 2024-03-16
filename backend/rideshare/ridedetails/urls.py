from django.urls import path
from . import views1

urlpatterns = [

    path('ridedetails/', views1.ridedetails, name='ridedetails'),
    # Add more URL patterns as needed
]