from select import select
from apps.home import blueprint
from flask import jsonify, render_template, request, session
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

@blueprint.route('/log', methods = ['GET', 'POST'])
@login_required
def log():
    data_log = ChangeLog.query.all()
    device_ids = []
    description_change = []
    time_change = []
    for i in range (-3,0):
        device_ids += [data_log[i].getDeviceID()]
        description_change += [data_log[i].getDcs_Change()]
        time_change += [data_log[i].getTime_Stamp()]
    return render_template('home/log.html', segment='log', bread_crumb = 'Log', len = len(device_ids), record_u = [device_ids, description_change, time_change])

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
