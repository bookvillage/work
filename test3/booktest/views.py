from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("好耶")


def get(request):
    di = request.GET
    a = di.getlist('a')
    b = di.get('b')
    context = {'a':a,'b':b}
    return render(request,'booktest/get.html',context)


def wishs(request):
    dict = request.POST
    name = dict.get('name')
    id = dict.getlist('id')
    wishs=['四季发财','绿树成荫','六六大顺','学习进步','早生贵子','吉祥如意']
    str = ''
    for i in id:
        id = int(i)
        str += wishs[id] + "---"
    context = {'name':name,'wish':str}
    return render(request,'booktest/wishs.html',context)

def wish(request):
    return render(request,'booktest/wish.html')

def post(request):
    if request.method == 'GET':
        return render(request,'booktest/post.html')
    elif request.method == 'POST':
        dict = request.POST
        username = dict.get('username')
        password = dict.get('password')
        gender = dict.get('gender')
        hobby = dict.getlist('hobby')  # 一键多值
        context = {
            'name': username,
            'pwd': password,
            'gender': gender,
            'hobby': hobby
        }
        return render(request, 'booktest/post1.html', context)
