from raspapp.controllers import amountController
from raspapp.libraries.stepper.instance import StepperInstance
from raspapp.models import Value

instance = StepperInstance()


def add_food():

    food_needed = is_food_needed()

    if food_needed:
        instance.do_add_food()

    return food_needed


def is_food_needed():

    threshold = Value.objects.get(name='food_threshold').value
    current_amount = amountController.get_food_amount()

    return current_amount < threshold

