from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/tcba'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Record(db.Model):
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
class User(db.Model):
    id_user = db.Column(db.Integer, primary_key = True)   
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    pass_word = db.Column(db.String(100))


class Device(db.Model):
    id_device = db.Column(db.Integer, primary_key = True)
    
if __name__ == "__main__":
    if not path.exists("user.db"):
        db.create_all(app = app)
        print("create database")
        

