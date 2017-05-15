import RPi.GPIO as GPIO
from time import sleep

from raspapp.models import Pin


class DCInstance:

    def __init__(self):

        self.Motor1A = Pin.objects.get(name='dc_a').number
        self.Motor1B = Pin.objects.get(name='dc_b').number
        self.Motor1E = Pin.objects.get(name='dc_enable').number


    def set_GPIO(self):

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.Motor1A, GPIO.OUT)
        GPIO.setup(self.Motor1B, GPIO.OUT)
        GPIO.setup(self.Motor1E, GPIO.OUT)


    def push_water(self):

        # Start DC motor

        GPIO.output(self.Motor1A, GPIO.HIGH)
        GPIO.output(self.Motor1B, GPIO.LOW)
        GPIO.output(self.Motor1E, GPIO.HIGH)

        sleep(4)


    def pull_water(self):

        # Start DC motor backwards to avoid extra water push.

        GPIO.output(self.Motor1A, GPIO.LOW)
        GPIO.output(self.Motor1B, GPIO.HIGH)
        GPIO.output(self.Motor1E, GPIO.HIGH)

        sleep(2)


    def stop_motor(self):

        GPIO.output(self.Motor1E, GPIO.LOW)


    def clean_GPIO(self):

        GPIO.cleanup()


    def do_add_water(self):

        self.set_GPIO()
        self.push_water()
        self.pull_water()
        self.stop_motor()
        self.clean_GPIO()
