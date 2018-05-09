# Author guomin

from django.contrib import admin
from django.urls import path,re_path
from cmdb import views

urlpatterns = [
    #path('cmdb2/',include("cmdb.urls")),

    path('admin/', admin.site.urls),
    path('login/', views.login),
    path('home/', views.home,name='home'),
    path('test/', views.test),
    #re_path('detail-(\d+).html', views.detail),
    re_path('detail-(?P<nid>\d+).html', views.detail),
    #http://127.0.0.1:8000/detail-2-9.html
    path('register/', views.Register.as_view()),

]
