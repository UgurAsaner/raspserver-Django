from raspapp.controllers import amountController
from raspapp.libraries.stepper.instance import StepperInstance
from raspapp.models import Value

instance = StepperInstance()


def add_food():

    if food_full():
        return False
    else:
        instance.feed()
        return True


def food_full():

    threshold = Value.objects.get(name='food_threshold').value
    current_amount = amountController.get_food_amount()

    if current_amount >= threshold:
        return False
    else:
        return True
