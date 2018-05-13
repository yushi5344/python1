# Author guomin
from django.utils.deprecation import MiddlewareMixin
class login_auth1(MiddlewareMixin):
    def process_request(self,request):
        print('第一个中间件请求')

    def process_view(self, request, view_func, view_func_args, view_func_kwargs):
        print('第一个中间件视图')
        print(view_func_args)
        print(request)
        print(view_func)
        print(view_func_args)

    def process_response(self,request,response):
        print('第一个中间件响应')
        return response

    #这个方法执行的条件是 views函数中有错误信息
    def process_exception(self,request,exception):
        print('出现异常')


class login_auth2(MiddlewareMixin):
    def process_request(self,request):
        print('第二个中间件请求')
    def process_response(self,request,response):
        print('第二个中间件响应')
        return response