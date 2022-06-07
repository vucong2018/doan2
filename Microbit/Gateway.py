
import serial.tools.list_ports
import random
import time
import sys
from Adafruit_IO import MQTTClient

AIO_FEED_ID = {"bbc-pump", "bbc-fan", "bbc-led", "bbc-mode"}
#
# AIO_USERNAME = "trongho912"
# AIO_KEY = "aio_oXwW17pj9GUjy3rCioqNINAIfG1K"

AIO_USERNAME_1 = "trongho912"
AIO_KEY_1 = "aio_fRTi73AmTn6IW6Wv275vdCiRUzfn"

AIO_USERNAME_2 = "hotrong912"
AIO_KEY_2 = "aio_ywrc83AY1VKkvstJvW2DG4kj4zIk"


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

# client = MQTTClient(AIO_USERNAME, AIO_KEY)
# client.on_connect = connected
# client.on_disconnect = disconnected
# client.on_message = message
# client.on_subscribe = subscribe
# client.connect()
# client.loop_background()


client1 = MQTTClient(AIO_USERNAME_1, AIO_KEY_1)
client2 = MQTTClient(AIO_USERNAME_2, AIO_KEY_2)

client1.on_connect = connected
client1.on_disconnect = disconnected
client1.on_message = message
client1.on_subscribe = subscribe
client1.connect()
client1.loop_background()

client2.on_connect = connected
client2.on_disconnect = disconnected
client2.on_message = message
client2.on_subscribe = subscribe
client2.connect()
client2.loop_background()


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
if getPort() == "None":  #hardcode for emulator
    ser = serial.Serial(port='COM4', baudrate=115200)
    isMicrobitConnected = True
elif getPort() != "None": #for real devices
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
            client1.publish("bbc-dht11-temp", VALUE_DATA)
        elif FIELD_DATA == "HUMID":
            client1.publish("bbc-dht11-humid", VALUE_DATA)
        elif FIELD_DATA == "LIGHT":
            client1.publish("bbc-light", VALUE_DATA)
        elif FIELD_DATA == "SOIL":
            client1.publish("bbc-soil", VALUE_DATA)
        elif FIELD_DATA == "LED":
            client1.publish("bbc-led-auto", VALUE_DATA)
        elif FIELD_DATA == "PUMP":
            client1.publish("bbc-pump-auto", VALUE_DATA)
        elif FIELD_DATA == "FAN":
            client1.publish("bbc-fan-auto", VALUE_DATA)
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
            if (end == len(mess)):
                mess = ""
            else:
                mess = mess[end+1:]


while True:
    if isMicrobitConnected:
        readSerial()
    time.sleep(1)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
