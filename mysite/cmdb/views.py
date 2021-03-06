from django.shortcuts import render,HttpResponse,redirect
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django import forms
from django.forms import widgets,fields
from cmdb import models
import json
import os
# Create your views here.
USER_LIST=[
    {'username':'张三','email':'42423@qq.com','gender':'男'}
]
for index in range(20):
    temp={'username':'张三'+str(index),'email':'42423@qq.com','gender':'男'}
    USER_LIST.append(temp)

def home(request):
    #获取cookie
    # v=request.COOKIES.get('username')
    #session判断原理
    #获取当前用户的随机字符串
    #根据字符串获取对应信息
    #根据对应信息查找is_login
    v=request.session.get('is_login',None)
    if not v:
        return redirect('/cmdb/login')
    else:
        userlist = models.UserInfo.objects.all()
        #<QuerySet [<UserInfo: UserInfo object (1)>, <UserInfo: UserInfo object (2)>, <UserInfo: UserInfo object (3)>, <UserInfo: UserInfo object (4)>]>
        #userlist是一个对象
        #userlist2=userlist.values('id','username','pwd')
        #userlist2是一个字典
        #<QuerySet [{'id': 1, 'username': 'guomin1232', 'pwd': '123456'}, {'id': 2, 'username': 'mam', 'pwd': '123456'}, {'id': 3, 'username': 'mamm', 'pwd': '123456'}, {'id': 4, 'username': 'lalal', 'pwd': '123456'}]>
        #userlist3=userlist.values_list('id','username','pwd','user_group__caption')
        #跨表操作 user_group__caption
        #userlist3是个元祖
        #<QuerySet [(1, 'guomin1232', '123456'), (2, 'mam', '123456'), (3, 'mamm', '123456'), (4, 'lalal', '123456')]>

        #print(userlist)
        #开始分页  每页显示2条
        pagesize=request.COOKIES.get('pagesize',None)
        if not pagesize:
            pagesize=1
        print(pagesize)
        paginator =Paginator(userlist,pagesize)#分页对象
        page = request.GET.get('page')
        try:
            contacts=paginator.page(page)
        except PageNotAnInteger:
            contacts=paginator.page(1)
        except EmptyPage:
            contacts=paginator.page(paginator.num_pages)
        return render(request, 'home.html', {'userlist': contacts})
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
    #请求头信息
    print(request.environ['HTTP_USER_AGENT'])
    if request.method=='POST':
        # cookie=False
        ret={'status':True,'error':None,'data':None}
        try:
            user = request.POST.get('username', None)
            pwd=request.POST.get('pwd',None)
            if user and len(user)>3:
                obj = models.UserInfo.objects.filter(username=user, pwd=pwd).first()
                if obj:
                    ret['status']=True
                    ret['error']='登录成功'
                    # cookie=True
                    #生成随机字符串
                    #写到用户浏览器cookie
                    #保存在session中
                    #在随机字符串对应的字典中设置相关内容
                    #Django将session保存在数据库中
                    request.session['username']=user
                    request.session['is_login']=True
                    if request.POST.get('auto_login',None)=='1':
                        request.session.set_expiry(3600*24*7)
                else:
                    ret['status']=False
                    ret['error']='用户名或密码错误'
            else:
                ret['status']=False
                ret['error']='用户名不得小于3位'
        except Exception as e:
            ret['status']=False
            ret['error']='请求错误'
        rep= HttpResponse(json.dumps(ret))
        # if cookie:
        #     rep.set_cookie('username',user,max_age=86400)#10分后失效
        return rep

    # if(request.method=='POST'):
    #     user=request.POST.get('username',None)
    #     pwd=request.POST.get('pwd',None)
    #     obj=models.UserInfo.objects.filter(username=user,pwd=pwd).first()
        #如果没有 为None，如果有 为对象
        #或者
        #count=models.UserInfo.objects.filter(username=user,pwd=pwd).count()
        # if obj:
        #     return redirect('/cmdb/home/')
        # else:
        #     error_msg='用户名密码不匹配'
        #     return render(request, 'login.html',{'error_msg':error_msg})
    else:
        return render(request, 'login.html')
class FormValidate(forms.Form):
    username=fields.CharField(
        label='用户名',
        initial='admin',
        error_messages={'required':'用户名不能为空','min_length':'用户名最少2位'},
        min_length=2)
    pwd=fields.CharField(
        label='密码',
        max_length=12,
        min_length=6,
        error_messages={'required':'密码不能为空','min_length':'密码不能小于6位','max_length':'密码不能大于12位'},
        widget=widgets.PasswordInput(attrs={'class':'pass'})
    )
    email=fields.EmailField(
        label='邮箱',
        error_messages={'required':'邮箱不能为空','invalid':'邮箱格式错误'}
    )
    city=fields.ChoiceField(
        choices=[(0,'上海'),(1,'广州'),(3,'南京')]
    )
    favor=fields.MultipleChoiceField(
        choices=[(1,'apple'),(2,'pea'),(3,'banana')]
    )
    provice=fields.CharField(
        initial=2,
        widget=widgets.RadioSelect(
            choices=((1,'上海'),(2,'厦门'))
        )
    )
#python中的CBV编程 Class-Base-Views
#FBV Function-Base-Views
from django.views import View
class Register(View):
    def get(self,request):
        data=FormValidate()
        return render(request,'register.html',{'data':data})
    def post(self,request):
        data=FormValidate(request.POST)
        res=data.is_valid()
        if res:
            print(data.cleaned_data)
            obj=models.UserInfo(**data.cleaned_data )
            obj.save()
            return render(request, 'login.html')
        else:
            print(data.errors)
            return render(request,'register.html',{'data':data})
        # username=request.POST.get('username',None)
        # pwd=request.POST.get('pwd',None)
        # email= request.POST.get('email')
        # models.UserInfo.objects.create(
        #     username=username,
        #     pwd=pwd,
        #     email=email
        # )
        #或者

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
#写上这个装饰器意味着不需要开启CSRF验证
@csrf_exempt
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


def addRole(request):
    if request.method=='POST':
        role_name=request.POST.get('role_name')
        obj=models.Role(
            role_name=role_name
        )
        obj.save()
        return redirect('/cmdb/showRole/')
    else:
        return render(request,'addRole.html')

def showRole(request):
    role_list=models.Role.objects.all()
    print(role_list)
    return render(request,'showRole.html',{'role_list':role_list})


def addAuth(request,nid):
    print(nid)
    role=models.Role.objects.filter(id=nid).first()
    print(role)
    #所有用户
    user_list=models.UserInfo.objects.all()
    print(user_list)
    return render(request,'addAuth.html',{'role':role,'user_list':user_list})

def saveAuth(request):
    role_id=request.POST.get('role_id')
    userinfo_id=request.POST.getlist('userinfo_id')
    print(role_id,userinfo_id)
    #开始保存到cmdb_role_au
    obj=models.Role.objects.get(id=role_id)
    print(obj)
    obj.au.add(*userinfo_id)
    return redirect('/cmdb/home')

#Django在前端显示数据时，如果要显示的数据带有html标签，则会显示成字符串
#这样做是为了防止XSS攻击
#可以使用管道操作符 safe 让其显示标签   {{html_tag|safe}}
#或者在后端使用mark_safe处理
#from django.utils.safestring import mark_safe
#html_tag=mark_safe(page_str)

#装饰器
#1CBV装饰器:
def auth(func):
    def inner(request,*args,**kwargs):
        return func(request,*args,**kwargs)
    return inner

def login_auth(request):
    v=request.COOKIES.get('username')
    if not v:
        return redirect('/cmdb/login')

def loginout(request):
    request.session.clear()
    return redirect('/cmdb/login')

from django.views.decorators.cache import cache_page
import time
#@cache_page(10)
def cache(request):
    t=time.time()
    return render(request,'cache.html',{'t':t})
