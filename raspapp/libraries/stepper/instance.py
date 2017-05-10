import RPi.GPIO as GPIO
import time
from raspapp.models import Pin, Value


class StepperInstance:

    def __init__(self):

        self.enable_pin = Pin.objects.get(name='stepper_enable').number
        self.coil_A_1_pin = Pin.objects.get(name='stepper_a1').number
        self.coil_A_2_pin = Pin.objects.get(name='stepper_a2').number
        self.coil_B_1_pin = Pin.objects.get(name='stepper_b1').number
        self.coil_B_2_pin = Pin.objects.get(name='stepper_b2').number
        self.steps = Value.objects.get(name='steps').value

    def forward(self, delay, steps):

        for i in range(0, steps):
            self.set_step(1, 0, 0, 1)
            time.sleep(delay)
            self.set_step(1, 0, 0, 0)
            time.sleep(delay)
            self.set_step(1, 1, 0, 0)
            time.sleep(delay)
            self.set_step(0, 1, 0, 0)
            time.sleep(delay)
            self.set_step(0, 1, 1, 0)
            time.sleep(delay)
            self.set_step(0, 0, 1, 0)
            time.sleep(delay)
            self.set_step(0, 0, 1, 1)
            time.sleep(delay)
            self.set_step(0, 0, 0, 1)
            time.sleep(delay)

    def backwards(self, delay, steps):

        for i in range(0, steps):
            self.set_step(0, 0, 0, 1)
            time.sleep(delay)
            self.set_step(0, 0, 1, 1)
            time.sleep(delay)
            self.set_step(0, 0, 1, 0)
            time.sleep(delay)
            self.set_step(0, 1, 1, 0)
            time.sleep(delay)
            self.set_step(0, 1, 0, 0)
            time.sleep(delay)
            self.set_step(1, 1, 0, 0)
            time.sleep(delay)
            self.set_step(1, 0, 0, 0)
            time.sleep(delay)
            self.set_step(1, 0, 0, 1)
            time.sleep(delay)

    def set_step(self, w1, w2, w3, w4):

        GPIO.output(self.coil_A_1_pin, w1)
        GPIO.output(self.coil_A_2_pin, w2)
        GPIO.output(self.coil_B_1_pin, w3)
        GPIO.output(self.coil_B_2_pin, w4)

    def set_GPIO(self):

        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.enable_pin, GPIO.OUT)
        GPIO.setup(self.coil_A_1_pin, GPIO.OUT)
        GPIO.setup(self.coil_A_2_pin, GPIO.OUT)
        GPIO.setup(self.coil_B_1_pin, GPIO.OUT)
        GPIO.setup(self.coil_B_2_pin, GPIO.OUT)
        GPIO.output(self.enable_pin, 1)

    def do_add_food(self):

        self.move()

    def move(self):

        steps = self.steps
        self.set_GPIO()
        self.backwards(1 / 1000.0, int(steps))
        self.forward(1 / 1000.0, int(steps))
        GPIO.cleanup()
