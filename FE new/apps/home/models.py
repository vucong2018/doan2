from os import device_encoding
from urllib3 import Retry
from apps import db
from datetime import datetime
class Record(db.Model):
    __tablename__ = 'Record'
    record_id = db.Column(db.Integer, primary_key = True)
    temp = db.Column(db.Integer)
    humi = db.Column(db.Integer)
    light = db.Column(db.Integer)
    soil = db.Column(db.Integer)
    time = db.Column(db.DateTime)
    def __init__(self, temp, humi, light, soil, time):
        self.temp = temp
        self.humi = humi
        self.light = light
        self.soil = soil
        self.time = time
    def __repr__(self):
        return str(self.temp) + ',' + str(self.humi) + ',' + str(self.light) + ',' +  str(self.soil) + ',' + str(self.time)
    
    def getData(self):
        return [str(self.temp) , str(self.humi) , str(self.light) , str(self.soil) , str(self.time)]
    def getTemp(self):
        return float(self.temp)
    def getHumi(self):
        return float(self.humi)
    def getLight(self):
        return float(self.light)
    def getSoil(self):
        return float(self.soil)
    def getTime(self):
        return str(self.time)
class ChangeLog(db.Model):
    __tablename__ = 'ChangeLog'
    device_id = db.Column(db.Integer)
    dcs_change = db.Column(db.String(1023))
    time_stamp = db.Column(db.DateTime, primary_key = True)
    def __init__ (self,device_id, dcs_change, time_stamp):
        self.device_id = device_id
        self.dcs_change = dcs_change
        self.time_stamp = time_stamp
    def getDeviceID(self):
        return self.device_id
    def getDcs_Change(self):
        return self.dcs_change
    def getTime_Stamp(self):
        return self.time_stamp
    def getFullLog(self):
        return [str(self.device_id), str(self.dcs_change), str(self.time_stamp)]

class Device(db.Model):
    __tablename__ = 'Device'
    device_id = db.Column(db.Integer, primary_key =  True)
    state = db.Column(db.Integer)
    def __init__(self, device_id, state):
        self.device_id = device_id
        