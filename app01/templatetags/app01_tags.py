from django import template
#调用template的一个装饰器library()，取名为register
register = template.Library()

#{{变量|filter_name:参数}}
@register.filter(name='s8')
def s8(value,arg):
    return value.replace(arg,'触不可及')

#add_age，这个name是这个函数的filename
@register.filter(name='add_age')
def add_age(value):
    return '年龄是:{}'.format(value)
