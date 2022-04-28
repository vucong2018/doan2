from select import select
from apps import db
from apps.home import blueprint
from flask import Response, flash, jsonify, render_template, request, session, json
from flask_login import login_required
from jinja2 import TemplateNotFound
from apps.home.models import Record, ChangeLog, Device

# import models

@blueprint.route('/index', methods = ['POST','GET'])
@login_required
def index():
    # [str(self.temp) , str(self.humi) , str(self.light) , str(self.soil) , str(self.time)]
    data = Record.query.all()
    record = data[-1].getData()
    
    return render_template('home/index.html', segment='index', bread_crumb = 'Dashboard', record_u = record)

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


@blueprint.route('/device-change/<d_id>', methods = ['GET', 'POST'])
@login_required
def change(d_id):
    dv_id = json.loads(d_id)
    device_change = Device.query.filter_by(device_id = dv_id).first()
    device_change.state = 1 if device_change.state == 0 else 0
    db.session.commit()
    return jsonify()

@blueprint.route('/log', methods = ['GET', 'POST'])
@login_required
def log():
    data_log = ChangeLog.query.all()
    name = 'Bao'
    device_ids = []
    description_change = []
    time_change = []
    for i in range (-3,0):
        device_ids += [data_log[i].getDeviceID()]
        description_change += [data_log[i].getDcs_Change()]
        time_change += [data_log[i].getTime_Stamp()]
    return render_template('home/log.html', segment='log', bread_crumb = 'Log', len = len(device_ids), name_u = name, record_u = [device_ids, description_change, time_change])

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
