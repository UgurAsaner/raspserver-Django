import requests
import uuid

from raspapp.controllers import sensorController as amounts
from raspapp.models import Server


def get_api_address():

     ip = Server.objects().filter(name='local').get().ip
     host = ip + '/piserver/piserver-laravel/public/'
     api_address = host + '/api/statuses'


def get_data():

    food_data = {
        'type': 'food',
        'amount': 1234
    }

    water_data = {
        'type': 'water',
        'amount': 12345
    }

    data = {
        'statuses': {
            food_data,
            water_data
        }
    }

    return data


def get_mac_id():

    mac_num = hex(uuid.getnode()).replace('0x', '').upper()
    mac = '-'.join(mac_num[i: i + 2] for i in range(0, 11, 2))

    return mac



def send_data():

    request = requests.post(get_api_address(), get_data(), header=[{'macId': get_mac_id()}])

    return request
