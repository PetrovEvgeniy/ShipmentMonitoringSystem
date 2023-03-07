import os
import requests
import json
import paho.mqtt.publish as publish
import ssl # we want to use secured web sockets

#from django_unixdatetimefield import UnixDateTimeField
from django.shortcuts import HttpResponse
from django.shortcuts import render_to_response
from myapp.models import *
from django.template import RequestContext

# Create your views here.
def index(request):

    # Connection method: use SSLWebsockets --->
    #tTransport = "websockets"
    #tPort = 443
    #tTSL = {'ca_certs':"/etc/ssl/certs/ca-certificates.crt",'tls_version':ssl.PROTOCOL_TLSv1}
    # <---

#     THINGSAPIGETKEY = "TWMWQQ9NV0EJN8UW"
#     CHANNELID = "1925304"
#     MQTT_HOST = "api.thingspeak.com"
# 
#     # Get the most actual channel feed
#     PAYLOAD_STRING = "{'api_key': '" + THINGSAPIGETKEY + "', 'results': '1'}"
#     JSON_PAYLOAD_STRING = PAYLOAD_STRING.replace("'", "\"")
#     GET_PAYLOAD = json.loads(JSON_PAYLOAD_STRING)
#     GET_REQUEST = "https://" + MQTT_HOST + "/channels/" + CHANNELID + "/feeds.json"
#     r = requests.get(GET_REQUEST , data=GET_PAYLOAD)

#     text = json.loads(r.text)
#     feed = text['feeds'][0]
#     channel = text['channel']
#     sensorName = channel['name']
#     creationDate = feed['created_at']
#     entryNumber = feed['entry_id']
#     temperature = feed['field2']
#     humidity = feed['field1']
#     accelX = feed['field3']
#     accelY = feed['field4']
#     accelZ = feed['field5']
#     latitude = feed['field6']
#     longitude = feed['field7']
#     
#     
#     latitude = '48.40885'
#     longitude = '9.95301'
    # Create a new database entry
    
    # Get most actual database entry
    tempData = TemperatureAndHumidityData.objects.order_by('-id')[0]
    creationDate = tempData.timestamp
    temperature = tempData.temperature
    humidity = tempData.humidity
    lat = tempData.lat
    lon = tempData.lon
    accelX = tempData.accelX
    accelY = tempData.accelY
    accelZ = tempData.accelZ
#    return HttpResponse("Myapp says hey there partner!")
    return render_to_response('index.html',{'creationDate':creationDate,'temperature': temperature, 'humidity': humidity,'accelX': accelX,'accelY': accelY,'accelZ': accelZ, 'lat': lat, 'lon': lon}, context_instance=RequestContext(request))
