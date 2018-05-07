from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello</h1>')

def login(request):
    # f=open('templates/login.html','r',encoding='utf-8')
    # data=f.read()
    # f.close()
    # return HttpResponse(data)
    if(request.method=='POST'):
        user=request.POST.get('username',None)
        pwd=request.POST.get('pwd',None)
        if(user=='admin' and pwd=='123'):
            return redirect('http://www.baidu.com')
        else:
            error_msg='用户名密码不匹配'
    return render(request, 'login.html',{'error_msg':error_msg})