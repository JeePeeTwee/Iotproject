# Introduction
I made a temperature and humidity sensor with my raspberry , this was done for the  class Datascience for IoT. I use a Raspberry Pi 3 A+ and a AM2302 Temp/Humidity Sensor

# The plan
I was wondering how hot it what the temperature and humidity would be in my room with my game computer. You would assume the same as the rest of the house since  the pc's are running in this room and they often generate heat, I was curious to see what the temperature would be and if the humidity would change.
To check the differences in temperature I placed the Pi and its sensor in the room with the game computer and compare that to the output of a similar devices  in the living room. I used Initial State bucket to read the result of the PI

# The progress
First I brainstormed how I would be measuring the temperature and looked at the options for sensors I had, I found many usable sensor but decided on an AM2302 Temp/Humidity Sensor. I did this cause I wasn’t sure if I wanted to solder and didn’t want to get a hat if I ended up wanting to Use it together with other sensors or items. I also bought a breadboard so I did not need to solder anything. I also used a T splitter to make it easier for myself to see where I connected the cables.
## The code
When I started with the code I started off by checking if the sensor was correctly plugged in and if it would work I used the documentation to check if I did everything correctly The code used to check was
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
This worked and printed the temperature and humidity in the console.

Then I wrote code to see how a connection to initial state IoT would work  I did this by using a set variable to see if I could get the exact same temperature back on the site, the code I wrote was
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
This also worked so I combined both pieces of code to get the end result which not only sends it to Inital State but also prints it out in the console so I could double check if it is sending the same data.

# Tutorial
## Things you will need
1. a raspberry pi (any from the 3 a+ or above will work
2. a AM2302 Temp/Humidity Sensor
3. a Initial State account (https://app.initialstate.com)
4. a breadboard (optional)
5. a 20 pin T splitter (optional)

## starting off
first you have to start by making a Initial State account.
once done create a new stream bucket by going to the side bar and pressing the create stream bucket button 
![image](https://github.com/JeePeeTwee/Iotproject/assets/158081202/9303b8d1-f7ef-4da1-ab82-3c503f106dcb) it’s the little cloud next to the search bar, give this bucket a name and press the create button on the bottom right of the create screen. 
After making a stream bucket go to the settings and note down the bucket name, bucket key and API endpoint.

![image](https://github.com/JeePeeTwee/Iotproject/assets/158081202/f3f45646-3c9e-4040-bbe3-422df4856d98)


## The setup
For the sensor itself you will need to connect it to the power, the ground and any of the other pins.
The red wire is the power, black the ground and the yellow wire you use for the input, note down hat pin the yellow wire is connected to for me it’s on pin 4
If you are using a T splitter and a breadboard it will look something like this
![Afbeelding van WhatsApp op 2024-01-31 om 13 56 18_0bb2c2e5](https://github.com/JeePeeTwee/Iotproject/assets/158081202/e748eda0-25f8-4cae-977d-f17cf0710f1c)



## The code
Ffor the code you can download the py file thats given in here you will need to set the streamer and the what pins u use for the pins u edit this part of the code
```py
dhtDevice = adafruit_dht.DHT22(board.D4,use_pulseio=False)
```
to edit what pin u use you write change the D4 i.e if you use pin 18 its board.D18

for the streaming to Initial State you edit
```py
 streamer = Streamer(bucket_name = "temperature", bucket_key = "VP4VD667DY6R" , access_key = "ist_SXF4wLmu-wj2dcSFuz4dQfWfAy_4WJMO")
```
you edit the bucket_name = "(the name of ur bucket)", bucket_key = "(the key u wrote down)" and acces_key = "(the Api key u wrote down)"
After doing all this the code should be working fine and you can log into Initial State and see the magic happen, it will look something like this
![image](https://github.com/JeePeeTwee/Iotproject/assets/158081202/b1182e06-a6b7-479a-b711-0aef5000a6ec)

If you want you can change the time it sends data to Initial State by changing the time.sleep(60) to anything else this is in seconds so make sure you edit those
