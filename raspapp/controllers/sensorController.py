from raspapp.libraries.sensor import instance
from raspapp.models import Pins

FOOD_SENSOR_DATA_PIN = Pins.objects.filter(name='food_sensor_data').number
FOOD_SENSOR_CLOCK_PIN = 19

def get_food_amount():

    instance.do_scale()

    pass