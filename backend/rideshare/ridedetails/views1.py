
from django.http import JsonResponse
from .models import Ride
from django.utils import timezone
import json

def ridedetails(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        source = data.get('source')
        destination = data.get('destination')
        estimatedAmount = data.get('estimatedAmount')
        print(source,destination,estimatedAmount)
        date = timezone.now().date()
        if source and destination and estimatedAmount:
            ride_details = Ride(source=source, destination=destination, estimatedAmount=estimatedAmount,date=date)
            ride_details.save()
            return JsonResponse({'message': 'Ride Booked successfully! Cab is on the way!!'})
        else:
            return JsonResponse({'error': 'source, destination, and estimatedAmount are required'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)
    

    #     ride = Ride.objects.create(source=source, destination=destination,amount=amount, date=date)
    #     return JsonResponse({'message': 'Ride details saved successfully!'})
    # else:
    #     return JsonResponse({'error': 'Invalid request method'}, status=400)