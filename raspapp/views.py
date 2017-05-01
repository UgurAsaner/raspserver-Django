from rest_framework.response import Response
from rest_framework.views import APIView

from raspapp.controllers import sensorController
from raspapp.cronjobs import functions


class Test(APIView):

    def get(self, request):

        return Response(functions.send_data())

class food(APIView):

    def get(self, request):

        return Response(sensorController.get_food_amount())

class water(APIView):

    def get(self, request):

        return Response(sensorController.get_water_amount())



