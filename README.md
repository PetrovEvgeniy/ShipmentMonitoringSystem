# 🛰️Shipment Monitoring System
Shipment Monitoring System was a team laboratory project that was part of the course "Internet of Things (IoT)" at THU. (2022)
  
## 💡Main Functionality (Raspbery PI)
- Collects sensor data (GPS, temperature, humidity, x-y-z acceleration) from Raspbery PI device, 
- Stores the data in the data in local file
- Publishes the last entry periodically (every 60 seconds) to the online Thingspeak API platform.

## 💡Main Functionality (Web Server)
- Subscribes to the Thingspeak API platform using mosquitto-sub python library
- Renders the last relevant data to a single web-page (transforms GPS data to a pin-point in an the map)
- Features LED OFF/ON button that toggles a LED on or off on the Raspberry device 

## 🛠️API Used
Thingspeak API (https://thingspeak.com)
OpenStreet API (https://wiki.openstreetmap.org)

## Project Architecture
<img src="https://i.imgur.com/OG88lkn.png" style="width: 30%, height:30%" alt="Project Architecture"  /> 

##Final result 
<img src="https://i.imgur.com/MUaxMtA.png" style="width: 30%, height:30%" alt="Application image"  />  

## ⚠️DISCLAIMER please do not use the featured API WRITE/READ keys 
