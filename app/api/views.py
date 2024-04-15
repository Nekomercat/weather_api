import requests
from .models import TravelTicket
from django.http import JsonResponse

# Create your views here.
def get_travel_tickets(request):
    travel_tickets = list(TravelTicket.objects.all().values())
    return JsonResponse({'travel_tickets': travel_tickets})

def get_weather_report(request):
    tickets = TravelTicket.objects.all()[:100]

    weather_reports = []
    for ticket in tickets:
        origin_latitude = ticket.origin_latitud
        origin_longitude = ticket.origin_longitud
        destination_latitude = ticket.destination_latitud
        destination_longitude = ticket.destination_longitud
        origin_city = ticket.origin
        destination_city = ticket.destination

        # Obtener el informe del clima para la ciudad de origen
        origin_weather = get_weather_for_city(origin_latitude,origin_longitude)
        
        # Obtener el informe del clima para la ciudad de destino
        destination_weather = get_weather_for_city(destination_latitude,destination_longitude)

        weather_report = {
        'ticket_id': ticket.id,
        'flight_num': ticket.flight_num,
        'origin_city': origin_city,
        'origin_weather': origin_weather,
        'destination_city': destination_city,
        'destination_weather': destination_weather
    }

        weather_reports.append(weather_report)

    return JsonResponse({'weather_reports': weather_reports})

def get_weather_for_city(latitude,longitude):
    WEATHER_API_KEY = "4b901c307a634116970233446241404"
    WEATHER_API_URL = "http://api.weatherapi.com/v1/current.json"

    params = {
        "key": WEATHER_API_KEY,
        "q": f"{latitude},{longitude}"
    }

    response = requests.get(WEATHER_API_URL, params=params)

    response.raise_for_status()
    weather_data = response.json()
    
    return weather_data