# Author guomin
from django import template
from django.utils.safestring import mark_safe
register=template.Library()

@register.simple_tag
def cal(a1,a2):
    return a1+a2

#自定义simple_tags
#1.在app下创建目录 templatetags
#2.在templatetags下创建任意py文件
#3 引入template 创建 register=template.Library()
#4 在函数上面写上 @register.simple_tag
#5 自定义函数
#6 在html顶部load该文件  {%load funcs %}

@register.filter
def comb(a1,a2):
    return a1+a2


#simple_tag和filter的优缺点
#simple_tag:
# 优点 ：可以穿传递多个参数，
#缺点 ：不能作为if条件