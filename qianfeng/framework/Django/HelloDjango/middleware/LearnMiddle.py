from django.utils.deprecation import MiddlewareMixin


class HelloMiddle(MiddlewareMixin):

    def process_request(self, request):
        print(request.META.get('REMOTE_ADDR'))
