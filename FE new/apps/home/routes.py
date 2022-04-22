from select import select
from apps.home import blueprint
from flask import jsonify, render_template, request, session
from flask_login import login_required
from jinja2 import TemplateNotFound
from apps.home.models import Record, ChangeLog

# import models

@blueprint.route('/index', methods = ['POST','GET'])
@login_required
def index():
    # [str(self.temp) , str(self.humi) , str(self.light) , str(self.soil) , str(self.time)]
    data = Record.query.all()
    record = data[-1].getData()
    
    
    return render_template('home/index.html', segment='index', record_u = record)

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
    return render_template('home/log.html', segment='index', len = len(device_ids), record_u = [device_ids, description_change, time_change])

@blueprint.route('/data', methods = ['POST','GET'])
@login_required
def temp_data_chart():
    data = Record.query.all()
    temp_data = [data[-7].getTemp(), data[-6].getTemp(),data[-5].getTemp(),data[-4].getTemp(), data[-3].getTemp(),data[-2].getTemp(),data[-1].getTemp()]
    humi_data = [data[-7].getHumi(), data[-6].getHumi(),data[-5].getHumi(),data[-4].getHumi(), data[-3].getHumi(),data[-2].getHumi(),data[-1].getHumi()]
    soil_data = [data[-7].getSoil(), data[-6].getSoil(),data[-5].getSoil(),data[-4].getSoil(), data[-3].getSoil(),data[-2].getSoil(),data[-1].getSoil()]
    light_data = [data[-7].getLight(), data[-6].getLight(),data[-5].getLight(),data[-4].getLight(), data[-3].getLight(),data[-2].getLight(),data[-1].getLight()]
    time_data = [data[-7].getTime(), data[-6].getTime(),data[-5].getTime(),data[-4].getTime(), data[-3].getTime(),data[-2].getTime(),data[-1].getTime()]
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
