#import RPi.GPIO as GPIO
import time
import sys
from .hx711 import HX711


def clean_GPIOs():

    GPIO.cleanup()


def setup_scale(data_pin, clock_pin):

    # Setting up the GPIO pins and the required constants for load sensor

    scale = HX711(data_pin, clock_pin)
    scale.set_reading_format("LSB", "MSB")
    scale.set_reference_unit(92)
    scale.reset()
    scale.tare()

    return scale


def do_scale(data_pin, clock_pin, num_of_measurements):

    # Declaration of fundamental variables.

    measurements = num_of_measurements
    estimated_exceptions = int(num_of_measurements / 3)
    exceptions = 0
    values = []
    scale = setup_scale(data_pin, clock_pin)

    # Capturing weight information in appropriate format.

    for i in range(measurements):

        val = scale.get_weight(1)
        values.append(int(-val / 5))

    clean_GPIOs()

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
