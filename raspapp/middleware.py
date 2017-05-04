
class Middleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def process_request(self, request):

        request_ip = request.META['REMOTE_ADDR']

        return request_ip

        # response = self.get_response(request)
        #
        # return response
