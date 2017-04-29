from rest_framework.response import Response
from rest_framework.views import APIView

from raspapp.cronjobs import functions


class Test(APIView):

    def get(self, request):

        return Response(functions.send_data())


