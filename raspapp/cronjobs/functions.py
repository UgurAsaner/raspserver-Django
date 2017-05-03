import requests
import uuid
from raspapp.models import Server, Status, Path
from raspapp.serializer import StatusSerializer
from raspapp.controllers import sensorController


def get_api_address():

    ip = Server.objects.get(name='piserver').ip
    path = Path.objects.get(name='status').path
    api_address = 'http://' + ip + path

    return api_address


def get_data():

    try:
        water_status = Status.objects.get(type='water')
        food_status = Status.objects.get(type='food')
    except Exception:
        water_status = Status()
        food_status = Status()

    water_status.type = 'water'
    water_status.amount = sensorController.get_water_amount()
    water_status.save()

    food_status.type = 'food'
    food_status.amount = sensorController.get_food_amount()
    food_status.save()

    serializer = StatusSerializer(Status.objects.all(), many=True)

    return serializer.data


def get_mac_id():

    mac_num = hex(uuid.getnode()).replace('0x', '').upper()
    mac_id = '-'.join(mac_num[i: i + 2] for i in range(0, 11, 2))

    return mac_id


def send_data():

    request = requests.post(get_api_address(), json=get_data(), headers={'Content-Type': 'application/json', 'macId': get_mac_id()})

    return request
