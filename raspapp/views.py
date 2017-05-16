from rest_framework.response import Response
from rest_framework.views import APIView
from raspapp.controllers import amountController, foodController, waterController
from raspapp.models import Server


class Test(APIView):

    def get(self, request):

        return Response(True)


class food(APIView):

    def get(self, request):

        return Response(amountController.get_food_amount())

    def post(self,request):

        return Response(foodController.add_food())


class water(APIView):

    def get(self, request):

        return Response(amountController.get_water_amount())

    def post(self, request):

        return Response(waterController.add_water())

