from django.db import models

# Create your models here.
class TravelTicket(models.Model):
    origin = models.CharField(max_length=3)
    destination = models.CharField(max_length=3)
    airline = models.CharField(max_length=2)
    flight_num = models.IntegerField()
    origin_iata_code = models.CharField(max_length=3)
    origin_name = models.CharField(max_length=100)
    origin_latitud = models.FloatField()
    origin_longitud = models.FloatField()
    destination_iata_code = models.CharField(max_length=3)
    destination_name = models.CharField(max_length=100)
    destination_latitud = models.FloatField()
    destination_longitud = models.FloatField()

    class Meta:
        db_table = 'travel_tickets'