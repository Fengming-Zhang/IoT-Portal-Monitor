# encoding=utf-8
from datetime import datetime
import sys
import json
import time
from flask import Flask, request
from flask_cors import *

sys.path.append('.')
import apis.aep_device_event
import apis.aep_device_status

app = Flask(__name__)
CORS(app, supports_credentials=True)

# product config
PRODUCT_ID = '15101463'
DEVICE_ID = '76afab91af78499582abc2b36c651cfc'
APP_KEY = 'TW8Xcu4tpfl'
APP_SECRET = '8KNtazD7Ae'
MASTER_API_KEY = '308fdaf1c5fb4ff1b020be995c54e26b'


@app.route('/api/temperature-humidity', methods=['GET'])
def get_temperature_humidity():
    temperature_json = json.dumps({
        'productId': PRODUCT_ID,
        'deviceId': DEVICE_ID,
        'datasetId': 'temperature_data'
    })
    humidity_json = json.dumps({
        'productId': PRODUCT_ID,
        'deviceId': DEVICE_ID,
        'datasetId': 'humidity_data'
    })

    temperature_data = apis.aep_device_status.QueryDeviceStatus(APP_KEY, APP_SECRET, temperature_json)
    humidity_data = apis.aep_device_status.QueryDeviceStatus(APP_KEY, APP_SECRET, humidity_json)

    result = json.dumps({
        'temperature': json.loads(temperature_data)['deviceStatus']['value'],
        'humidity': json.loads(humidity_data)['deviceStatus']['value']
    })

    print('--------------')
    print(result)
    return result


@app.route('/api/monitor', methods=['GET'])
def monitor():
    invade_indecator = 0
    cur_timestamp = int(time.time())
    # print(cur_timestamp)
    body_json = json.dumps({
        'productId': PRODUCT_ID,
        'deviceId': DEVICE_ID,
        'startTime': cur_timestamp - 5,
        'endTime': cur_timestamp,
        'pageSize': '10'
    })
    monitor_response = apis.aep_device_event.QueryDeviceEventList(APP_KEY, APP_SECRET, MASTER_API_KEY, body_json)
    monitor_list = json.loads(monitor_response)['result']['list']
    # print('----------------')
    # print(monitor_list)
    for event_dict in monitor_list:
        event_content = json.loads(event_dict['eventContent'])
        if event_content['ir_sensor_data'] == 1:
            invade_indecator = 1
            break
    print('----------------')
    print(invade_indecator)
    # print(monitor_response)

    result = json.dumps({
        'invade_indecator': invade_indecator
    })
    return result

@app.route('/api/monitor/period', methods=['GET'])
def monitor_period():
    invades = []
    today = datetime.date.today()
    for i in range(1, 8):
        date = today - datetime.timedelta(days=i)
        # print(date.strftime("%Y-%m-%d") + " 00:00:00")
        # print(date.strftime("%Y-%m-%d") + " 23:59:59")
        start_timestamp = time.mktime(time.strptime(date.strftime("%Y-%m-%d") + " 00:00:00",'%Y-%m-%d %H:%M:%S'))
        end_timestamp = time.mktime(time.strptime(date.strftime("%Y-%m-%d") + " 23:59:59",'%Y-%m-%d %H:%M:%S'))
        # print(start_timestamp)
        # print(end_timestamp)
        body_json = json.dumps({
            'productId': PRODUCT_ID,
            'deviceId': DEVICE_ID,
            'startTime': start_timestamp,
            'endTime': end_timestamp,
            'pageSize': '10'
        })
        monitor_response = apis.aep_device_event.QueryDeviceEventList(APP_KEY, APP_SECRET, MASTER_API_KEY, body_json)
        monitor_list = json.loads(monitor_response)['result']['list']
        invade_indicator = 0
        for event_dict in monitor_list:
            event_content = json.loads(event_dict['eventContent'])
            if event_content['ir_sensor_data'] == 1:
                invade_indicator += 1
        # print('----------------')
        # print(invade_indicator)
        invades.append(invade_indicator)
    # print(invades)

    ret = '['
    for invade in invades:
        ret += str(invade) + ','
    ret = ret[:-1] + ']'
    # print(ret)
    return ret

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)