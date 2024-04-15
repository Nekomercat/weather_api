from .models import TravelTicket
from django.http import JsonResponse

# Create your views here.
def get_travel_tickets(request):
    travel_tickets = list(TravelTicket.objects.all().values())
    return JsonResponse({'travel_tickets': travel_tickets})