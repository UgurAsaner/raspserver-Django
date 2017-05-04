from raspapp.libraries.sensor.instance import SensorInstance


instance = SensorInstance()


def get_food_amount():

    return instance.food_scale(num_of_measurements=9)


def get_water_amount():

    return instance.water_scale(num_of_measurements=9)
