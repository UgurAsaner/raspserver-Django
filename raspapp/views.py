from django.shortcuts import render
from rest_framework.response import Response

from raspapp.cronscripts import functions
from rest_framework.views import APIView


class Test(APIView):

    def get(self):

        return Response('hi')


