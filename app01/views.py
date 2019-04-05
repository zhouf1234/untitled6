from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse

# Create your views here.

#FBV方式：函数方式
def login(request):
    if request.method == "POST":
        print(request.POST)
    #return HttpResponse('ok')
    return render(request,'login.html')

#CBV方式：类的方式
#View基类的对应
from django.views import View
class Login(View):
    #get获取数据
    def get(self,request):
        print(request.body)
        print("=" *120)
        print(request.path)
        print("=" *120)
        print(request.encoding)
        print("=" *120)
        return render(request,'login.html')
    #post返回信息
    def post(self,request):
        #print(request.body)
        #print("=" *120)
        #print(request.path)
        #print("-" *120)
        #print(request.encoding)
        #print("*" *120)
        #print(request.get_host())
        #print("+" * 120)
        #print(request.get_full_path())
        #print("~" * 120)
        #print(request.POST.getlist("num2"))
        #print("=" * 120)
        #print(request.POST)
        print(request.FILES)
        #request.FILES["file"]代表上传的文件在request.FILES里面，name代表取到对象名字
        filename = request.FILES["file"].name
        #这个with写入，把传入的文件传到了本文件夹下，看一看
        with open(filename,"wb")as f:
            for i in request.FILES["file"].chunks():
                #用chunks()不用read()读取是为了保证文件不会大量使用系统内存，html的form一定要写enctype属性
                f.write(i)
        #当在login的提交按钮按了以后，会跳出的内容是hello
        res = HttpResponse('hello')
        #HttpResponse.content：响应内容
        #HttpResponse.charset：响应内容的编码
        #HttpResponse.status_code：响应的状态码
        print(res.content)
        print(res.charset)
        print(res.status_code)
        res['Content-Type'] = 'text/html; charset=UTF-8'
        print(res.charset)
        return HttpResponse(res)
        #return HttpResponse('hello')

#JsonResponse的方法返回一个字典，之前的返回ok都是字符串

def userinfo(request):
    data = {"name":"珊珊","dream":"write a book"}
    data1= [{"name": "珊珊", "dream": "write a book"}]
    #"status":0状态代表ok，1代表异常
    data2={"status":0,"data":[{"name":"alex","dream":"write a book"}],"error":"请先登录"}
    #如果写成return HttpResponse(data)，返回的内容是字典的key
    # 给下方的json导入的模块
    #import json
    #return HttpResponse(json.dumps(data))

    #显示的结果和json的一样，但是字体不一样;字典有中文，结果是unicode码;只能传递字典类型，json的就不一样了
    #return JsonResponse(data)
    #如果要传递非字典类型需要设置一下safe关键字参数。
    #return JsonResponse(data1,safe=False)
    return JsonResponse(data2)

def template_test(request):
    s1 = "dandan nihao nihenpiaoliang dandan"
    l = ["lili","bobo","coco"]
    d = {"name":"cici","age":20}
    s2= "<a href='http://www.jd.com/'>点击</a>"
    #s3="<script>for (){alert(123):}</script>"
    s4="在苍茫的大海上，狂风卷积着乌云，在乌云和大海间，海燕像黑色的闪电。"
    import datetime
    now = datetime.datetime.now()
    class Person(object):
        def __init__(self,name):
            #实例化传对象，一个name参数,传给name
            self.name = name
        def dream(self):
            return "{}的梦想是成为明星".format(self.name)
    #实例化类对象lili,bobo,coco,给他们绑定传值Lili，Bobo,Coco
    lili = Person("Lili")
    bobo = Person("Bobo")
    coco = Person("Coco")
    l2 = [lili,bobo,coco]

    filesize = 123456
    #return render(request,'template_test.html',{"s1":s1,"l":l,"d":d,"l2":l2,"filesize":filesize,"now":now})
    #locals全局变量，意为全部上传
    return render(request, 'template_test.html',locals())

#测试继承模板
def class_list(request):
    return render(request, 'class_list.html')

def teacher_list(request):
    return render(request, 'teacher_list.html')