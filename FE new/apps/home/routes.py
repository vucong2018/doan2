from datetime import date, datetime
from datetime import datetime, date
from select import select
from turtle import delay
from apps import db
from apps.home import blueprint
from flask import Response, flash, jsonify, render_template, request, session, json
from flask_login import current_user, login_required
from jinja2 import TemplateNotFound
from apps.home.models import Record, ChangeLog, Device
# 
from datetime import datetime, timedelta

from distutils.command.clean import clean
import random
import re
import time
import  sys
from  Adafruit_IO import  Client



AIO_FEED_IDS = ["bbc-pump", "bbc-fan", "bbc-led", "bbc-mode"]
AIO_USERNAME = "hotrong912"
AIO_KEY = "aio_YYDV05rnlYYHu5PrzJ5b8UjgIi9d"
client = Client(AIO_USERNAME, AIO_KEY)

# def changeToSever(feed_name, value):
#     client.publish(feed_name, value)


# client = MQTTClient(AIO_USERNAME, AIO_KEY)






# 
# from sever import changeToSever

# import models

@blueprint.route('/index', methods = ['POST','GET'])
@login_required
def index():
    # [str(self.temp) , str(self.humi) , str(self.light) , str(self.soil) , str(self.time)]
    data = Record.query.all()
    record = data[-1].getData()
    
    return render_template('home/index.html', segment='index', bread_crumb = 'Dashboard', record_u = record, user = current_user)

@blueprint.route('/device', methods = ['POST','GET'])
@login_required
def device():
    device = Device.query.all()
    device_id = []
    device_state = []
    for i in range (-3, 0):
        device_id += [device[i].getID()]
        device_state += [device[i].getState()]
    return jsonify({'device_id': device_id,
                    'device_state': device_state})

# ADD MY FUNC
@blueprint.route('/device-change/<d_id>', methods = ['GET', 'POST'])
# DEVICE CHANGE
@login_required
def change(d_id):
    dv_id = json.loads(d_id)
    device_change = Device.query.filter_by(device_id = dv_id).first()
    
    print(dv_id)
        
    
    device_change.state = 1 if device_change.state == 0 else 0
    if dv_id == 101:
        # delay(1)
        client.send_data("bbc-pump", device_change.state)
    elif dv_id == 102:
        client.send_data("bbc-fan", device_change.state)
    elif dv_id == 103:
        client.send_data("bbc-led", device_change.state)
        
    db.session.commit()
    return jsonify(d_id)

@blueprint.route('/log', methods = ['GET', 'POST'])
@login_required
def log():
    data_log = ChangeLog.query.all()
    device_ids = []
    human = []
    description_change = []
    time_change = []
    for i in range (-10,0):
        device_ids += [data_log[-11-i].getDeviceID()]
        human += [data_log[-11-i].getHumanName()]
        description_change += [data_log[-11-i].getDcs_Change()]
        time_change += [data_log[-11-i].getTime_Stamp()]
    return render_template('home/log.html', segment='log', bread_crumb = 'Log', len = len(device_ids), record_u = [device_ids, description_change, human, time_change])

@blueprint.route('/log/<string:data_log>', methods = ['GET', 'POST'])
@login_required
def add_log(data_log):
    info = json.loads(data_log)
    add_log = ChangeLog(info['device_id'], info['human'], info['descript'], datetime.now())
    db.session.add(add_log)
    db.session.commit()
    # print()
    return jsonify(data_log)


@blueprint.route('/data', methods = ['POST','GET'])
@login_required
def temp_data_chart():
    data = Record.query.all()
    temp_data = [] 
    humi_data = []
    soil_data = []
    light_data = []
    time_data = []
    for i in range (-7,0):
        temp_data += [data[i].getTemp()] 
        humi_data += [data[i].getHumi()]
        soil_data += [data[i].getSoil()]
        light_data += [data[i].getLight()]
        time_data += [data[i].getTime()]
    return jsonify({'temp_list': temp_data,
                    'humi_list': humi_data,
                    'soil_list': soil_data,
                    'light_list': light_data,
                    'time_list': time_data})
    
@blueprint.route('/data_month', methods = ['POST','GET'])
@login_required
def Data_get_month():
    # cur_time = datetime.datetime.utcnow()
    
    #data_month = Record.query.filter(Record.time < cur_time - datetime.datetime.timedelta(weeks = 4)).all()
    last_month = date.today() + timedelta(days = - 20)
    data_month = Record.query.filter(Record.time > last_month ).all()
    # temp_data += [data[i].getTemp()] 
    # humi_data += [data[i].getHumi()]
    # soil_data += [data[i].getSoil()]
    # light_data += [data[i].getLight()]
    # time_data += [data[i].getTime()]
    list_humi = [row.getHumi() for  row in data_month]
    list_light = [row.getLight() for  row in data_month]
    list_soil = [row.getSoil() for  row in data_month]
    list_temp = [row.getTemp() for  row in data_month]
    list_time = [row.getTime() for  row in data_month]
    return str(list_humi)
@blueprint.route('/<template>')
@login_required
def route_template(template):

    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
