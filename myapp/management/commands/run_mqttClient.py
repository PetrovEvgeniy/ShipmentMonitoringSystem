from django.core.management.base import BaseCommand, CommandError
from myapp.models import *

import os
import sys
import django
import json
import paho.mqtt.client as mqtt
import time
import datetime

class Command(BaseCommand):
    help = 'Invokes the mqtt client and subscribes to the thingspeak server'

    def handle(self, *args, **options):

    # ---- Enter your code below.......!


	def on_connect(client, userdata, flags, rc):
    		print("Connected with result code: " + str(rc))

	def on_message(client, userdata, message):
    		print("message topic:       " + message.topic)
    		print("message received:    " + str(message.payload.decode("utf-8")))
    		msg = json.loads(str(message.payload.decode("utf-8")))

    		channel =      msg['channel_id'] 
    		creationDate = msg['created_at']
    		entryNumber =  msg['entry_id']
    		humidity =     msg['field1']
    		temperature =  msg['field2']
    		accelx =       msg['field3']
    		accely =       msg['field4']
    		accelz =       msg['field5']
    		latitude =     msg['field6']
    		longitude =    msg['field7']

    		# Create a new database entry
    		table = TemperatureAndHumidityData()
                table.timestamp = creationDate
    		table.temperature = temperature
    		table.humidity = humidity
    		table.lat = latitude
    		table.lon = longitude
    		table.accelX = accelx
    		table.accelY = accely
    		table.accelZ = accelz
    		table.save()

	def on_log(client, userdata, level, buf):
    		print("log: " + buf)

	# ThingSpeak MQTT Broker: do not change
	MQTTHOST = "mqtt3.thingspeak.com"

	#Channel ID: Enter your channel id!
	CHANNELID = "1968587"

	#ThingSpeak Read Key: Enter your personal read key!
	THINGSAPIKEY_READ ="1VVZLQ26YOPRFGOI"

	#MQTT client name: Enter a unique but arbitrary string!
	CLIENT_NAME = "HiE2Lzk5OhYLMR0INBMWLyg"

	#ThingSpeaks standard MQTT port number: do not change
	PORT=1883

	#Some additional parameters: leave these values unchanged
	KEEPALIVE=600
	QOS_LEVEL=0

#---->student123!
#Insert your code: 
#use the predefined parameters,
#create a mqtt paho client 
#and attach the appropriate callback functions;
#don't forget to invoke the "username_pw_set()" function 
#with the username and ThingSpeak API key 
#in advance to the call of the "connect()" function;
#subscribe to your ThingSpeak channel
#and use "loop_forever()" at the end of your program
#instead of the loop_start()/loop_stop() method!

	Connected = False
	client = mqtt.Client(CLIENT_NAME)
	client.username_pw_set(username = CLIENT_NAME, password = "1etPcBftdhftlD4Sp5GBUGMY")
	client.on_connect = on_connect
	client.on_message = on_message

	client.connect(MQTTHOST, PORT)
	client.loop_start()

	#while Connected != True:
		#time.sleep (0.1)

	client.subscribe("channels/"+ CHANNELID +"/subscribe")

	try:
		while True:
			time.sleep(1)

	except KeyboardInterrupt:
		print "exiting"
		client.disconnect()
		client.loop_stop()
	client.loop_forever()
		
