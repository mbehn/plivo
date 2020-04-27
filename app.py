from flask import Flask, render_template, request, redirect, url_for
import plivo
import configparser, math
app = Flask(__name__)


config = configparser.ConfigParser()
config.read('configuration.conf')
auth_id = config['plivo']['auth_id'].strip('\'')
auth_token = config['plivo']['auth_token'].strip('\'')
src_number = config['plivo']['src_number'].strip('\'')

client = plivo.RestClient(auth_id=auth_id, auth_token=auth_token)

@app.route('/')
def index():
    if request.args.get('data'):
        message_info = request.args.get('data')
        return render_template('index.html', data=message_info)
    return render_template('index.html')

@app.route('/sendmessage', methods=['POST'])
def sendmessage():
    if request.method == 'POST':
        data = request.form    
        message_created = client.messages.create(
            src=src_number,
            dst='+1' + data.get('phone'),
            text=data.get('message')
        )
        return redirect(url_for('index', data=message_created.message_uuid))
    return render_template('sendmessage.html', data=message_created)

@app.route('/getmessages', methods=['POST','GET'])
def getmessages():
    if request.method == 'POST':
        data = request.form
        messages = client.messages.list(message_time__gte=str(data['from-date']) + " 00:00", message_time__lte=str(data['to-date']) + " 23:59", limit=20)
        total_message_count = messages.meta.total_count
        page_count = math.ceil(total_message_count/20)
        print(page_count)
        return render_template('message_list.html', data=data, messages=messages, from_date=data['from-date'], to_date=data['to-date'], total_message_count=total_message_count, page_count=page_count)
    if request.method == 'GET':
        try:
            data = request.args
            messages = client.messages.list(message_time__gt=str(data['from_date']) + " 00:00", message_time__lt=str(data['to_date']) + " 23:59", offset=data['page'], limit=20)
            total_message_count = messages.meta.total_count
            page_count = math.ceil(total_message_count/20)        
            return render_template('message_list.html', data=data, messages=messages, from_date=data['from_date'], to_date=data['to_date'], total_message_count=total_message_count, page_count=page_count)
        except:
            return render_template('message_list.html')