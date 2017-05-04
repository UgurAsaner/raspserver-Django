
class Middleware(object):

    def process_request(self, request):

        request_ip = request.META['REMOTE_ADDR']

        return request_ip


