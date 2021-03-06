# import serial.tools.list_ports
from datetime import datetime
import model
from distutils.command.clean import clean
import random
import re
import time
import  sys
from  Adafruit_IO import  MQTTClient



AIO_FEED_IDS = ["bbc-dht11-humid", "bbc-dht11-temp", "bbc-light", "bbc-soil", "fan", "led", "rainulator"]
AIO_USERNAME = "trongho912"
AIO_KEY = "aio_fRTi73AmTn6IW6Wv275vdCiRUzfn"






def connected(client):
    print("Ket noi thanh cong...")
    for feed_id in AIO_FEED_IDS:
        client.subscribe(feed_id)

def subscribe(client, userdata, mid, granted_qos):
    print ("Subscribe thanh cong...")

def disconnected(client):
    print("Ngat ket noi...")
    sys.exit(1)
record = {
    'humi' : 'None',
    'temp' : 'None',
    'soil' : 'None',
    'light': 'None',
}
def recordIsFull(record):
    for key in record:
        if record[key] == 'None':
            return False   
    return True

def add_data_record (key, payload, record):
    if record[key] == 'None':
        record[key] = payload
        
    
    if recordIsFull(record):
        #QUERY FOR DATABASE
        u_record = model.Record(temp = record['temp'], humi = record['humi'], soil = record['soil'], light = record['light'], time = datetime.today())
        model.db.session.add(u_record)
        model.db.session.commit()
        print("Record Full")
        record['humi'] = 'None'
        record['temp'] = 'None'
        record['light'] = 'None'
        record['soil'] = 'None'
        
                    
def message(client, feed_id, payload):
    if feed_id == 'bbc-dht11-humid':
        print('bbc-dht11-humid is comming...: ' + payload)
        add_data_record ('humi', payload, record)
    elif feed_id == 'bbc-dht11-temp':
        print('bbc-dht11-temp is comming...: ' + payload)
        add_data_record ('temp', payload, record)
    elif feed_id == 'bbc-light':
        print('bbc-light is comming...: ' + payload)
        add_data_record ('light', payload, record)
    elif feed_id == 'bbc-soil':
        print('bbc-soil is comming...: ' + payload)
        add_data_record ('soil', payload, record)
    elif feed_id == 'fan':
        print('fan is comming...: ' + payload)
    elif feed_id == 'led':
        print('led is comming...: ' + payload)
    elif feed_id == 'rainulator':
        print('raiulator is comming...: ' + payload)
        
client = MQTTClient(AIO_USERNAME, AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()


while True:
    pass
    