from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
USER_LIST=[
    {'username':'张三','email':'42423@qq.com','gender':'男'}
]
for index in range(20):
    temp={'username':'张三'+str(index),'email':'42423@qq.com','gender':'男'}
    USER_LIST.append(temp)

def home(request):
    if(request.method=='POST'):
        username=request.POST.get('username',None)
        email=request.POST.get('email',None)
        gender=request.POST.get('gender',None)
        temp={'username':username,'email':email,'gender':gender}
        USER_LIST.append(temp)
    return render(request,'home.html',{'userlist':USER_LIST})


def login(request):
    # f=open('templates/login.html','r',encoding='utf-8')
    # data=f.read()
    # f.close()
    # return HttpResponse(data)
    if(request.method=='POST'):
        user=request.POST.get('username',None)
        pwd=request.POST.get('pwd',None)
        if(user=='admin' and pwd=='123'):
            return redirect('/home/')
        else:
            error_msg='用户名密码不匹配'
            return render(request, 'login.html',{'error_msg':error_msg})