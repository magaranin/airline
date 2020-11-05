from django.db import models

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures") 
    #models.ForeignKey = is used to call other class Airport is from our class. 
    # models.CASCADE- if deleted from tabel is going to delete from corresponding flights 
    #related_name - when we want to use in reverse order 
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals") 
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"