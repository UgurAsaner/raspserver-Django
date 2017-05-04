from raspapp.models import Value
from raspapp.libraries.dc.instance import DCInstance
import amountController

instance = DCInstance()


def add_water():

    if water_full():
        return False
    else:
        instance.do_add_water()
        return True


def water_full():

    threshold = Value.objects.get(name='water_threshold').value
    current_amount = amountController.get_water_amount()

    if current_amount >= threshold:
        return True
    else:
        return False
