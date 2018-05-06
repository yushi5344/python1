from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello</h1>')

def login(request):
    # f=open('templates/login.html','r',encoding='utf-8')
    # data=f.read()
    # f.close()
    # return HttpResponse(data)
    return render(request,'login.html')