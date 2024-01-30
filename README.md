# introduction
I made a temperature and humidity sensor, this was done for my class Datascience for IoT with a raspberry pi 3 A+ and a AM2302 Temp/Humidity Sensor

# The plan
I was wondering how hot it would be in my room with my computer. You would asume the same as around the rest of the house but due to its location and the pc's running i was curious to see what the temperature would be and if the humidity would change.
To check the differences in temperature I would be letting the Pi and its sensor run in the other room and then with use of the initial state bucket I used I could check the Temperature from the living room where the thermostat is located.

# The progress
first 
## the code
when i started with the code I started off by checking if the sensor was correctly plugged in and if it would work I used the documentation to check if I did everything correctly The code used to check was
```py
import time 
import board
import adafruit_dht

#sets the pin for the sensor and sets use pulseio to false cause that could lead to trouble with raspberry pi's
dhtDevice = adafruit_dht.DHT22(board.D4,use_pulseio=False)  

#loops the temperature and humidity sensor check every 4 seconds and prints it out
while True:
    try:
        temp_c = dhtDevice.temperature
        humidity = dhtDevice.humidity
        print("Temp:{:.1f} C    Humidity: {}% ".format(temp_c, humidity))
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(4.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error

    time.sleep(4.0)
```
this worked and printed the temperature and humidity in the console.

Then i wrote code to see how a connection to initial state IoT would work i did this by using a set variable to see if i could get the exact same temperature back on the site, the code i wrote was
```py
import time 
import board
import adafruit_dht
import sys
import os
from ISStreamer.Streamer import Streamer


#sets the pin for the sensor and sets use pulseio to false cause that could lead to trouble with raspberry pi's
dhtDevice = adafruit_dht.DHT22(board.D4,use_pulseio=False)
def main():
    #sets the code for the streamer so it knows what to reach and send data to 
    streamer = Streamer(bucket_name = "temperature", bucket_key = "VP4VD667DY6R" , access_key = "ist_SXF4wLmu-wj2dcSFuz4dQfWfAy_4WJMO")
 while True:
        try:
            temp_c = 20
            humidity = 50
            streamer.log("Temperatuur", temp_c)
            streamer.log("vochtigheid %", humidity)
            streamer.flush
            time.sleep(60)
```
this also worked so i combined both pieces of code to get the end result which not only sends it to Inital State but also prints it out to double check.
