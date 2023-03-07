from __future__ import unicode_literals

from django.db import models

# Create your models here.
class TemperatureAndHumidityData(models.Model):
    timestamp = models.CharField(max_length=26)
    temperature = models.CharField(max_length=5)
    humidity = models.CharField(max_length=5)
    lat = models.CharField(max_length=10)
    lon = models.CharField(max_length=10)
    accelX = models.CharField(max_length=10,default = "")
    accelY = models.CharField(max_length=10,default = "")
    accelZ = models.CharField(max_length=10,default = "")
    
    def __unicode__(self):
        return self.timestamp  
    def __str__(self):
        return "lat: " + self.lat + "  long: " + self.lon
