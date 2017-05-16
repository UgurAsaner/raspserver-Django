from raspapp.models import Value
from raspapp.libraries.dc.instance import DCInstance
import amountController

instance = DCInstance()


def add_water():

    food_needed = is_water_needed()

    if food_needed:
        instance.do_add_water()

    return food_needed


def is_water_needed():

    threshold = Value.objects.get(name='water_threshold').value
    current_amount = amountController.get_water_amount()

    return current_amount < threshold
