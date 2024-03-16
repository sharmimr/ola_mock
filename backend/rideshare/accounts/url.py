from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('check-user/', views.check_user, name='check_user'),
]