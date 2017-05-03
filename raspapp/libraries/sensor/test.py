import sys
from instance import SensorInstance

instance = SensorInstance()

while True:

    try:

        print 'Water:' + str(instance.water_scale())

        print 'Food:' + str(instance.food_scale())


    except KeyboardInterrupt:
        sys.exit()
