from django.shortcuts import render,HttpResponse,redirect
from cmdb import models
import os
# Create your views here.
USER_LIST=[
    {'username':'张三','email':'42423@qq.com','gender':'男'}
]
for index in range(20):
    temp={'username':'张三'+str(index),'email':'42423@qq.com','gender':'男'}
    USER_LIST.append(temp)

def home(request):

    userlist = models.UserInfo.objects.all()
    #<QuerySet [<UserInfo: UserInfo object (1)>, <UserInfo: UserInfo object (2)>, <UserInfo: UserInfo object (3)>, <UserInfo: UserInfo object (4)>]>
    #userlist是一个对象
    userlist2=userlist.values('id','username','pwd')
    #userlist2是一个字典
    #<QuerySet [{'id': 1, 'username': 'guomin1232', 'pwd': '123456'}, {'id': 2, 'username': 'mam', 'pwd': '123456'}, {'id': 3, 'username': 'mamm', 'pwd': '123456'}, {'id': 4, 'username': 'lalal', 'pwd': '123456'}]>
    userlist3=userlist.values_list('id','username','pwd','user_group__caption')
    #跨表操作 user_group__caption
    #userlist3是个元祖
    #<QuerySet [(1, 'guomin1232', '123456'), (2, 'mam', '123456'), (3, 'mamm', '123456'), (4, 'lalal', '123456')]>

    print(userlist3)
    return render(request, 'home.html', {'userlist': userlist})
    # if(request.method=='POST'):
    #     username=request.POST.get('username',None)
    #     email=request.POST.get('email',None)
    #     gender=request.POST.get('gender',None)
    #     favor=request.POST.getlist('favor')
    #     print(favor)
    #     #文件上传
    #     obj=request.FILES.get('imgs')
    #     print(obj,type(obj),obj.name)
    #     file_path=os.path.join('upload',obj.name)
    #     f=open(file_path,mode='wb')
    #     for i in obj.chunks():
    #         f.write(i)
    #     f.close()
    #     temp={'username':username,'email':email,'gender':gender}
    #     USER_LIST.append(temp)
    # return render(request,'home.html',{'userlist':USER_LIST})


def login(request):
    if(request.method=='POST'):
        user=request.POST.get('username',None)
        pwd=request.POST.get('pwd',None)
        obj=models.UserInfo.objects.filter(username=user,pwd=pwd).first()
        #如果没有 为None，如果有 为对象
        #或者
        #count=models.UserInfo.objects.filter(username=user,pwd=pwd).count()
        if obj:
            return redirect('/cmdb/home/')
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
        models.UserInfo.objects.create(
            username=username,
            pwd=pwd,
            email=email
        )
        #或者
        # obj=models.UserInfo(
        #     username=username,
        #     pwd=pwd,
        #     email=email
        # )
        # obj.save()
        return  render(request,'login.html')
USERLIST={
        '1':{'name':'root','email':'root@qq.com'},
        '2':{'name':'root','email':'root@qq.com'},
        '3':{'name':'root','email':'root@qq.com'},
        '4':{'name':'root','email':'root@qq.com'},
        '5':{'name':'root','email':'root@qq.com'},
    }
def test(request):
    return render(request,'test.html',{'userlist':USERLIST})

def detail(request,nid):
    #details=USERLIST[nid]
    #re_path('detail-(?P<nid>\d+)-(?P<uid>\d+).html', views.detail),
    #def detail(request,**kwargs):
       #kwargs={'nid':1,'uid':3}
    #def detail(request,*args,**kwargs):
        #args=(2,9)
    details=models.UserInfo.objects.filter(id=nid).first()
    userGroup=models.UserGroup.objects.all()
    print(userGroup)
    return render(request,'detail.html',{'detail':details,'user_group':userGroup})


#数据新增、
# models.UserInfo.objects.create(
#         username=username,
#         pwd=pwd,
#         email=email
#     )
#或者
# obj=models.UserInfo(
#     username=username,
#     pwd=pwd,
#     email=email
# )
# obj.save()


#数据查询
#查询所有
#result=models.UserInfo.objects.all()
#结果是对象
#条件查询
#result=models.UserInfo.objects.filter(username='root')
#删除
#models.UserInfo.objects.filter(username='root').delete()
#更新
#models.UserInfo.objects.filter(username='root').update(password='123')

def update(request):
    username=request.POST.get('username',None)
    email=request.POST.get('email',None)
    ids=request.POST.get('id',None)
    user_group_id=request.POST.get('user_group_id')
    result=models.UserInfo.objects.filter(id=ids).update(
        username=username,
        email=email,
        user_group_id=user_group_id
    )
    print(result)
    return redirect('/cmdb/home')

def delete(request,nid):
    result=models.UserInfo.objects.filter(id=nid).delete()
    print(result)
    return redirect('/cmdb/home')