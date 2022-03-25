# import serial.tools.list_ports
from datetime import datetime
import model
from distutils.command.clean import clean
import random
import re
import time
import  sys
from  Adafruit_IO import  MQTTClient



AIO_FEED_IDS = ["bbc-dht11-humi", "bbc-dht11-temp", "bbc-light", "bbc-soil", "fan", "led", "rainulator"]
AIO_USERNAME = "vucong2018"
AIO_KEY = "aio_ARPK90JrZ5WSm9dG8wsV0TVAKU4y"






def connected(client):
    print("Ket noi thanh cong...")
    for feed_id in AIO_FEED_IDS:
        client.subscribe(feed_id)

def subscribe(client, userdata, mid, granted_qos):
    print ("Subscribe thanh cong...")

def disconnected(client):
    print("Ngat ket noi...")
    sys.exit(1)

        
                    
def message(client, feed_id, payload):
    print("Is change...")
        
client = MQTTClient(AIO_USERNAME, AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()


while True:
    value_humi = random.randint(0,90)
    value_temp = random.randint(0,50)
    value_light = random.randint(0,1023)
    value_soil = random.randint(0,1023)
    client.publish("bbc-dht11-humi", value_humi)
    client.publish("bbc-dht11-temp", value_temp)
    client.publish("bbc-light", value_light)
    client.publish("bbc-soil", value_soil)
    time.sleep(15)
    