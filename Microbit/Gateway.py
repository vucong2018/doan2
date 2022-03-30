# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import serial.tools.list_ports
import random
import time
import sys
from Adafruit_IO import MQTTClient

AIO_FEED_ID = {"bbc-pump", "bbc-fan", "bbc-led", "bbc-mode"}
AIO_USERNAME = "trongho912"
AIO_KEY = "aio_oXwW17pj9GUjy3rCioqNINAIfG1K"


def connected(client):
    print("Ket noi thanh cong...")
    for feed in AIO_FEED_ID:
        client.subscribe(feed)


def subscribe(client, userdata, mid, granted_qos):
    print("Subcribe thanh cong...")


def disconnected(client):
    print("Ngat ket noi...")
    sys.exit(1)


def message(client, feed_id, payload):
    print("Nhan du lieu: " + feed_id + ": " + payload)
    code = "!" + feed_id + ":" + payload + '#'
    if isMicrobitConnected:
        ser.write((str(code)).encode())


client = MQTTClient(AIO_USERNAME, AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()


def getPort():
    ports = serial.tools.list_ports.comports()
    N = len(ports)
    commPort = "None"
    for i in range(0, N):
        port = ports[i]
        strPort = str(port)
        if "USB Serial Device" in strPort:
            splitPort = strPort.split(" ")
            commPort = (splitPort[0])
    return commPort


isMicrobitConnected = False
if getPort() != "None":
    ser = serial.Serial(port=getPort(), baudrate=115200)
    isMicrobitConnected = True

mess = ""


def processData(data):
    data = data.replace("!", "")
    data = data.replace("#", "")
    splitData = data.split(":")
    print(splitData)
    FIELD_DATA = splitData[0]
    VALUE_DATA = splitData[1]
    try:
        if FIELD_DATA == "TEMP":
            client.publish("bbc-dht11-temp", VALUE_DATA)
        # elif FIELD_DATA == "HUMID":
        #     client.publish("bbc-dht11-humid", VALUE_DATA)
        elif FIELD_DATA == "LIGHT":
            client.publish("bbc-light", VALUE_DATA)
        elif FIELD_DATA == "SOIL":
            client.publish("bbc-soil", VALUE_DATA)
        elif FIELD_DATA == "LED":
            client.publish("bbc-led-auto", VALUE_DATA)
        elif FIELD_DATA == "PUMP":
            client.publish("bbc-pump-auto", VALUE_DATA)
        elif FIELD_DATA == "FAN":
            client.publish("bbc-fan-auto", VALUE_DATA)
    except:
        pass


def readSerial():
    bytesToRead = ser.inWaiting()
    if (bytesToRead > 0):
        global mess
        mess = mess + ser.read(bytesToRead).decode("UTF-8")
        while ("#" in mess) and ("!" in mess):
            start = mess.find("!")
            end = mess.find("#")
            processData(mess[start:end + 1])
            # print(me)
            if (end == len(mess)):
                mess = ""
            else:
                mess = mess[end+1:]


while True:
    if isMicrobitConnected:
        readSerial()
    time.sleep(1)
    # value_humid = random.randint(0, 90)
    # value_temp = random.randint(0, 50)
    # value_light = random.randint(0, 1023)
    # value_soil = random.randint(0, 1023)
    # client.publish("bbc-dht11-humid", value_humid)
    # client.publish("bbc-dht11-temp", value_temp)
    # client.publish("bbc-light", value_light)
    # client.publish("bbc-soil", value_soil)
    # time.sleep(15)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
