# import serial.tools.list_ports

from datetime import datetime

from distutils.command.clean import clean
import random
import re
import time
import  sys
from  Adafruit_IO import  MQTTClient



AIO_FEED_IDS = ["bbc-pump", "bbc-fan", "bbc-led", "bbc-mode"]
AIO_USERNAME = "hotrong912"
AIO_KEY = "aio_coTD17WUnijiug5VUX0hnP5QmrQH"


def changeToSever(feed_name, value):
    client.publish(feed_name, value)



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
# client.loop_background()

def changeToSever(feed_name, value):
    client.publish(feed_name, value)

# while True:
#     value_humi = random.randint(20,90)
#     value_temp = random.randint(1,50)
#     value_light = random.randint(1,1023)
#     value_soil = random.randint(1,1023)
#     client.publish("bbc-dht11-humi", value_humi)
#     client.publish("bbc-dht11-temp", value_temp)
#     client.publish("bbc-light", value_light)
#     client.publish("bbc-soil", value_soil)
#     time.sleep(15)
    # pass
    
