import requests
import threading
import concurrent.futures
from .models import TravelTicket
from django.http import JsonResponse
from concurrent.futures import ThreadPoolExecutor

api_semaphore = threading.BoundedSemaphore(value=5)

# Create your views here.
def get_travel_tickets(request):
    travel_tickets = list(TravelTicket.objects.all().values())
    return JsonResponse({'travel_tickets': travel_tickets})

def get_weather_report(request):
    tickets = TravelTicket.objects.all()[:100]

    weather_reports = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_ticket = {executor.submit(get_weather_for_ticket, request, ticket): ticket for ticket in tickets}

        for future in concurrent.futures.as_completed(future_to_ticket):
            ticket = future_to_ticket[future]
            try:
                weather_report = future.result()
                weather_reports.append(weather_report)
            except Exception as exc:
                # Manejar excepciones si ocurren
                print(f'Error al procesar el ticket {ticket.id}: {exc}')

    return JsonResponse({'weather_reports': weather_reports})

def get_weather_for_ticket(request, ticket):
    origin_latitude = ticket.origin_latitud
    origin_longitude = ticket.origin_longitud
    destination_latitude = ticket.destination_latitud
    destination_longitude = ticket.destination_longitud
    origin_city = ticket.origin
    destination_city = ticket.destination

    origin_weather = get_weather_for_city(origin_latitude,origin_longitude)

    destination_weather = get_weather_for_city(destination_latitude,destination_longitude)

    weather_report = {
        'ticket_id': ticket.id,
        'flight_num': ticket.flight_num,
        'origin_city': origin_city,
        'origin_weather': origin_weather,
        'destination_city': destination_city,
        'destination_weather': destination_weather
    }

    return weather_report

def get_weather_for_city(latitude,longitude):
    WEATHER_API_KEY = "4b901c307a634116970233446241404"
    WEATHER_API_URL = "http://api.weatherapi.com/v1/current.json"

    params = {
        "key": WEATHER_API_KEY,
        "q": f"{latitude},{longitude}"
    }

    with api_semaphore:
        response = requests.get(WEATHER_API_URL, params=params)

    response.raise_for_status()
    weather_data = response.json()
    
    return weather_data