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
    