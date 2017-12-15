from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime, timedelta
import random
from bookvillage.models import BookInfo,HeroInfo


# Create your views here.
def nihao(request):
    return HttpResponse('<h1>你好</h1>')


def setcookie(request):
    # response = HttpResponse("设置cookie")
    response = HttpResponseRedirect("/getcookie")
    response.set_cookie('num1','123',max_age=10)
    # response.set_cookie('num2', '234', expires=datetime.now() + timedelta(days=7))
    return response

def getcookie(request):
    dict = request.COOKIES
    str = ''
    if 'num1' in dict:
        str = "cookie的值是" + dict['num1']
    else:
        str = '没有cookie值'
    return HttpResponse(str)

def set_session(request):
    request.session['username']='mike'
    request.session.set_expiry(3600)
    return HttpResponse('设置session')

def get_session(request):
    session = request.session.get('username')
    return HttpResponse('session的值是'+ session)

def delsession(request):
    # request.session.clear()
    request.session.flush()
    return HttpResponse('删除session')

def bookprice(request):
    datas = BookInfo.objects.all()
    for data in datas:
        data.price = random.randint(30,58)
    return render(request,'bookvillage/bookprice.html',{'datas':datas})

def login(request):
    return render(request, 'bookvillage/login.html')

from PIL import Image, ImageDraw, ImageFont
from django.utils.six import BytesIO

def verify(request):
    #引入随机函数模块
    import random
    #定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(
        20, 100), 255)
    width = 100
    height = 25
    #创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    #创建画笔对象
    draw = ImageDraw.Draw(im)
    #调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    #定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    #随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    #构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
    font = ImageFont.truetype('Tamil MN.ttc', 23)
    #构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    #绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    #释放画笔
    del draw
    #存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    #内存文件操作
    print(rand_str)
    buf = BytesIO()
    #将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    #将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')

def login_check(request):
    post = request.POST
    name = post.get('username')
    pwd = post.get('password')
    # 获取用户输入的验证码
    veri = post.get('verify')

    # 从session读取已存的验证码
    sess = request.session.get('verifycode')

    # 比较用户名、密码、和验证码
    if name == 'tom' and pwd == '123456' and veri == sess:
        return HttpResponse('<h2>恭喜登陆成功！</h2>')
    else:
        return HttpResponse('<h2>登录失败！请重试！</h2>')