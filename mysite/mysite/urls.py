"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path,include

urlpatterns = [
    #路由分发
    #如果有多个模块，可以在顶级路由文件中写 include方法
    #然后分配到各个模块中
    #在每个模块中，应该有一个urls.py文件 c处理当前模块的路由
    # 路由访问 http://127.0.0.1:8000/cmdb/login/
    path('cmdb/',include("cmdb.urls")),
    #path('cmdb2/',include("cmdb.urls")),

]
