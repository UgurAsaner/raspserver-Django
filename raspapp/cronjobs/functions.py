import requests
import uuid

from raspapp.models import Server, Status
from raspapp.serializer import StatusSerializer


def get_api_address():

    ip = Server.objects.filter(name='local').first().ip
    host = ip + '/piserver/piserver-laravel/public'
    api_address = 'http://' + host + '/api/status'

    return api_address




def get_data():

    try:
        water_status = Status.objects.get(type='water')
        food_status = Status.objects.get(type='food')
    except Exception:
        water_status = Status()
        food_status = Status()

    water_status.type = 'water'
    water_status.amount = '132'
    water_status.save()

    food_status.type = 'food'
    food_status.amount = '12312'
    food_status.save()

    serializer = StatusSerializer(Status.objects.all(), many=True)

    return serializer.data


def get_mac_id():

    mac_num = hex(uuid.getnode()).replace('0x', '').upper()
    mac = '-'.join(mac_num[i: i + 2] for i in range(0, 11, 2))

    return mac



def send_data():

    request = requests.post(get_api_address(), json=get_data(), headers={'Content-Type': 'application/json', 'macId': get_mac_id()})

    return request
