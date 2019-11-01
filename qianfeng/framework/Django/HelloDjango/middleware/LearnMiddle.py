from django.utils.deprecation import MiddlewareMixin


class HelloMiddle(MiddlewareMixin):

    # 过滤请求
    def process_request(self, request):
        print(request.META.get('REMOTE_ADDR'))

    # 异常处理
    def process_exception(self, request, exception):
        print('request', exception)
