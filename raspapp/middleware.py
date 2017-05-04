from rest_framework.response import Response
from django.core.exceptions import PermissionDenied
from raspapp.models import Server


class Middleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        request_ip = request.META['REMOTE_ADDR']
        allowed_ip = Server.objects.get(name='piserver').ip

        if request_ip is not allowed_ip:
            raise PermissionDenied

        response = self.get_response(request)

        return response


