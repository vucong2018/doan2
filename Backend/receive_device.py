# import serial.tools.list_ports
from datetime import datetime
from turtle import up

from flask_sqlalchemy import Model
import model
from distutils.command.clean import clean
import random
import re
import time
import  sys
from sqlalchemy import update
from  Adafruit_IO import  MQTTClient


AIO_FEED_IDS = ["bbc-pump", "bbc-fan", "bbc-led", "bbc-mode"]
AIO_USERNAME = "hotrong912"
AIO_KEY = "aio_YYDV05rnlYYHu5PrzJ5b8UjgIi9d"






def connected(client):
    print("Ket noi thanh cong...")
    for feed_id in AIO_FEED_IDS:
        client.subscribe(feed_id)

def subscribe(client, userdata, mid, granted_qos):
    print ("Subscribe thanh cong...")

def disconnected(client):
    print("Ngat ket noi...")
    sys.exit(1)

def update_device (key_1, payload):
    model.Device.query.all()[key_1].state = payload
    model.db.session.commit()
    model.db.session
    
                    
def message(client, feed_id, payload):
    if feed_id == 'bbc-pump':
        update_device(0, payload)
    elif feed_id == 'bbc-led':
        update_device(1, payload)
    elif feed_id == 'bbc-led':
        update_device(2, payload)
        
        
client = MQTTClient(AIO_USERNAME, AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()




while True:
    pass

# print(model.Device.query.all()[0].state)

    