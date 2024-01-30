import time 
import board
import adafruit_dht
import sys
import os
from ISStreamer.Streamer import Streamer


dhtDevice = adafruit_dht.DHT22(board.D4,use_pulseio=False)
def main():
    streamer = Streamer(bucket_name = "temperature", bucket_key = "VP4VD667DY6R" , access_key = "ist_SXF4wLmu-wj2dcSFuz4dQfWfAy_4WJMO")
    
    while True:
        try:
            temp_c = dhtDevice.temperature
            humidity = dhtDevice.humidity
            print("Temp:{:.1f} C    Humidity: {}% ".format(temp_c, humidity))
            streamer.log("Temperatuur", temp_c)
            streamer.log("vochtigheid %", humidity)
            streamer.flush
            time.sleep(60)
        except RuntimeError as error:
            print(error.args[0])
            time.sleep(4.0)
            continue
        except Exception as error:
            dhtDevice.exit()
            raise error

        time.sleep(4.0)
if __name__ == '__main__':
    main()