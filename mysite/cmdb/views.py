from django.shortcuts import render,HttpResponse,redirect
import os
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
        favor=request.POST.getlist('favor')
        print(favor)
        #文件上传
        obj=request.FILES.get('imgs')
        print(obj,type(obj),obj.name)
        file_path=os.path.join('upload',obj.name)
        f=open(file_path,mode='wb')
        for i in obj.chunks():
            f.write(i)
        f.close()
        temp={'username':username,'email':email,'gender':gender}
        USER_LIST.append(temp)
    return render(request,'home.html',{'userlist':USER_LIST})


def login(request):
    if(request.method=='POST'):
        user=request.POST.get('username',None)
        pwd=request.POST.get('pwd',None)
        if(user=='admin' and pwd=='123'):
            return redirect('/home/')
        else:
            error_msg='用户名密码不匹配'
            return render(request, 'login.html',{'error_msg':error_msg})
    else:
        return render(request, 'login.html')
#python中的CBV编程 Class-Base-Views
#FBV Function-Base-Views
from django.views import View
class Register(View):
    def get(self,request):
        return render(request,'register.html')
    def post(self,request):
        username=request.POST.get('username',None)
        pwd=request.POST.get('pwd',None)
        email= request.POST.get('email')

        return  render(request,'register.html',{'username':username,'pwd':pwd,'email':email})
