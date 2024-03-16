# views.py
from django.http import JsonResponse
from .models import User
import json

def signup(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        if username and email and password:
            user = User(username=username, email=email, password=password)
            user.save()
            return JsonResponse({'message': 'User created successfully'})
        else:
            return JsonResponse({'error': 'Username, email, and password are required'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

def check_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        print(username)
        if User.objects.filter(username=username).exists():
            print ("123")
            return JsonResponse({'user_exists': True,'username':username})
        else:

            print ("0003")
            return JsonResponse({'user_exists': False})