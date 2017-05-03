import RPi.GPIO as GPIO
from hx711 import HX711
from raspapp.models import Pin, Value


class SensorInstance:

    def __init__(self):

        self.FOOD_SENSOR_DATA_PIN = Pin.objects.get(name='food_data').number
        self.FOOD_SENSOR_CLOCK_PIN = Pin.objects.get(name='food_clock').number
        self.WATER_SENSOR_DATA_PIN = Pin.objects.get(name='water_data').number
        self.WATER_SENSOR_CLOCK_PIN = Pin.objects.get(name='water_clock').number

        self.FOOD_TARE = Value.objects.get(name='food_tare').value
        self.WATER_TARE = Value.objects.get(name='water_tare').value

    def clean_GPIOs(self):

        GPIO.cleanup()

    def setup_scale(self, data_pin, clock_pin):

        # Setting up the GPIO pins and the required constants for load sensor

        scale = HX711(data_pin, clock_pin)
        scale.set_reading_format("LSB", "MSB")
        scale.set_reference_unit(92)

        return scale

    def food_scale(self, num_of_measurements=15):

        data_pin = self.FOOD_SENSOR_DATA_PIN
        clock_pin = self.FOOD_SENSOR_CLOCK_PIN
        tare = self.FOOD_TARE

        return self.do_scale(self, data_pin, clock_pin, num_of_measurements, tare)

    def water_scale(self, num_of_measurements=15):

        data_pin = self.WATER_SENSOR_DATA_PIN
        clock_pin = self.WATER_SENSOR_CLOCK_PIN
        tare = self.WATER_TARE

        return self.do_scale(self, data_pin, clock_pin, num_of_measurements, tare)

    def do_scale(self, data_pin, clock_pin, num_of_measurements, tare):

        # Declaration of fundamental variables.

        scale = self.setup_scale(data_pin, clock_pin)
        measurements = num_of_measurements
        estimated_exceptions = int(num_of_measurements / 3)
        exceptions = 0
        values = []

        # Capturing weight information in appropriate format.

        for i in range(measurements):
            scale.power_down()
            scale.power_up()
            val = scale.get_weight(1)
            meaning_val = int(-val / 5) + tare
            values.append(meaning_val)

        self.clean_GPIOs()

        # Removing exceptions if any exist.

        for i in range(estimated_exceptions):
            if min(values):
                values.remove(min(values))
                exceptions += 1
            if max(values):
                values.remove(max(values))
                exceptions += 1

        # Calculating the mean for the rest of values.

        result = sum(values) / (measurements - exceptions)

        return result
