from raspapp.libraries.sensor import instance
from raspapp.models import Pins

FOOD_SENSOR_DATA_PIN = Pins.objects.get(name='food_sensor_data').number
FOOD_SENSOR_CLOCK_PIN = Pins.objects.get(name='food_sensor_clock').number
WATER_SENSOR_DATA_PIN = Pins.objects.get(name='water_sensor_data').number
WATER_SENSOR_CLOCK_PIN = Pins.objects.get(name='water_sensor_clock').number


def get_food_amount():

    return instance.do_scale(FOOD_SENSOR_DATA_PIN, FOOD_SENSOR_CLOCK_PIN, 15)


def get_water_amount():

    return instance.do_scale(WATER_SENSOR_DATA_PIN, WATER_SENSOR_CLOCK_PIN, 15)
