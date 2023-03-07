#!/usr/bin/env python

import time
import os
import requests
import json
import paho.mqtt.client as mqtt

Connected = False #global variable for the state of the connection

def on_connect(client, userdata, flags, rc):
    print("Connected with result code: " + str(rc))
    client.subscribe("channels/1925304")
    Connected = True


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


def on_log(client, userdata, level, buf):
    print("log: " + buf)

# ThingSpeak MQTT Broker: do not change
THINGS_DEVICE_MQTTSERV = "mqtt3.thingspeak.com"

#Channel ID: Enter your channel id!
CHANNELID = "1925304"

#ThingSpeak Device user name: Enter your personal user name!
THINGS_DEVICE_USERNAME = "KwUABBcFEQQwLTQ3LyEEHjU"

#ThingSpeak Device password: Enter your password!
THINGS_DEVICE_PASSWORD = "X358xFsnRTNt+rVaUVN2l81F"

#ThingSpeak Device client id: Enter the client id!
CLIENT_NAME = "KwUABBcFEQQwLTQ3LyEEHjU"

#ThingSpeaks standard MQTT port number: do not change
PORT=1883

#Some additional parameters: leave these values unchanged
KEEPALIVE=600
QOS_LEVEL=0

#---->
#Insert your code: 
#use the predefined parameters,
#create a mqtt paho client 
#and attach the appropriate callback functions;
#don't forget to invoke the "username_pw_set()" function 
#with the username and password 
#in advance to the call of the "connect()" function;
#subscribe to your ThingSpeak channel
#and use "loop_forever()" at the end of your program
#instead of the loop_start()/loop_stop() method!
Connected = False #global variable for the state of the connection


client = mqtt.Client("KwUABBcFEQQwLTQ3LyEEHjU") #create new instance
client.username_pw_set(THINGS_DEVICE_USERNAME, password=THINGS_DEVICE_PASSWORD) #set username and password
client.on_connect= on_connect #attach function to callback
client.on_message= on_message #attach function to callback

client.connect(THINGS_DEVICE_MQTTSERV, port=PORT) #connect to broker

client.loop_start() #start the loop

while Connected != True: #Wait for connection
    time.sleep(0.1)
    print Connected
    client.subscribe("channels/1925304")

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print "exiting"
    client.disconnect()
    client.loop_stop()




