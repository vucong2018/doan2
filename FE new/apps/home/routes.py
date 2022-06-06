from datetime import date, datetime
from distutils.command.config import config
from fileinput import filename
from urllib import response
# from select import select
# from turtle import delay
from apps import db, mysql
from apps.home import blueprint
from flask import Response, flash, jsonify, make_response, redirect, render_template, request, session, json, url_for
from flask_login import current_user, login_required
from jinja2 import TemplateNotFound
from apps.home.models import Record, ChangeLog, Device, DataLimit
# 
from datetime import datetime, timedelta
from flaskext.mysql import MySQL
import pymysql
import io
import csv
import pdfkit
#
from distutils.command.clean import clean
import random
import re
import time
import sys
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
    data_limit = DataLimit.query.all()
    temp_data = [] 
    humi_data = []
    soil_data = []
    light_data = []
    time_data = []
    limit_data = []
    for i in range (-7,0):
        temp_data += [data[i].getTemp()] 
        humi_data += [data[i].getHumi()]
        soil_data += [data[i].getSoil()]
        light_data += [data[i].getLight()]
        time_data += [data[i].getTime()]
    for i in range (0,4):
        limit_data += [data_limit[i].getLimit()]
    return jsonify({'temp_list': temp_data,
                    'humi_list': humi_data,
                    'soil_list': soil_data,
                    'light_list': light_data,
                    'time_list': time_data,
                    'limit': limit_data})

@blueprint.route('/limit-change/<string:limit>', methods = ['GET', 'POST'])
@login_required
def change_limit(limit):
    data = json.loads(limit)
    elem_change = DataLimit.query.filter_by(element = data['element']).first()
    elem_change.limit_value = data['limit_value']
    # add_log = ChangeLog(info['device_id'], info['human'], info['descript'], datetime.now())
    # db.session.add(add_log)
    db.session.commit()
    # print()
    return jsonify(limit)

@blueprint.route('/report', methods = ['POST','GET'])
@login_required
def show_report():
    return render_template('home/report.html', segment='report', bread_crumb = 'Report')

@blueprint.route('/report/<int:num_time>', methods = ['POST','GET'])
@login_required
def Data_get_month(num_time):
    # cur_time = datetime.datetime.utcnow()
    
    #data_month = Record.query.filter(Record.time < cur_time - datetime.datetime.timedelta(weeks = 4)).all()
    last_month = date.today() + timedelta(days = - num_time)
    data_month = Record.query.filter(Record.time > last_month ).all()
    list_humi = [row.getHumi() for  row in data_month]
    list_light = [row.getLight() for  row in data_month]
    list_soil = [row.getSoil() for  row in data_month]
    list_temp = [row.getTemp() for  row in data_month]
    list_time = [row.getTime() for  row in data_month]
    return jsonify({'temp_list': list_temp,
                    'humi_list': list_humi,
                    'soil_list': list_soil,
                    'light_list': list_light,
                    'time_list': list_time})

# @blueprint.route('/report/print/<int:num_time>', methods = ['POST','GET'])
# @login_required
# def print_pdf(num_time):
#     data = Data_get_month(num_time).json
#     rendered = render_template('home/report_print.html', len = len(data['humi_list']), record = data)
#     path_l = b'D:\\do_not_open\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
#     config = pdfkit.configuration(wkhtmltopdf= path_l)
#     pdf = pdfkit.from_string(rendered, 'Mypdf.pdf', configuration=config)

#     res = make_response(pdf)
#     res.headers['Content-Type'] = 'application/pdf'
#     res.headers['Content-Disposition'] = 'inline'

#     return rendered

@blueprint.route('/download/report/csv/<int:num_time>', methods = ['POST','GET'])
@login_required
def DownLoadCSV(num_time):
    conn = None
    cursor = None

    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
    
        if num_time == 30: cursor.execute("SELECT * FROM record WHERE DATEDIFF(CURDATE(), time) < 30")
        if num_time == 60: cursor.execute("SELECT * FROM record WHERE DATEDIFF(CURDATE(), time) < 60")
        if num_time == 90: cursor.execute("SELECT * FROM record WHERE DATEDIFF(CURDATE(), time) < 90")
        result = cursor.fetchall()
        output = io.StringIO()
        writer = csv.writer(output)
        line = ['Id, Temp, Humi, Light, Soil, Time']
        writer.writerow(line)
        for row in result:
            line = [str(row['record_id']) + ',' + str(row['temp']) + ',' + str(row['humi']) + ',' + str(row['light'])+ ',' + str(row['soil'])+ ',' + str(row['time'])]
            writer.writerow(line)
        output.seek(0)
        return Response(output, mimetype="text/csv", headers ={"Content-Disposition":"attachment;filename=employee_report.csv"})
    except Exception as e:
        print(e)
        return "Error" + e
    finally:
        cursor.close() 
        conn.close()

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
