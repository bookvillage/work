from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from booktest.models import BookInfo,HeroInfo

def index(request):
    return HttpResponse("<h1>iii</h1>")


def index1(request):
    books = BookInfo.objects.all()
    context = {'books':books}
    return render(request,"booktest/index.html",context)

def index2(request,bid):
    book= BookInfo.objects.get(id=bid)
    heros = book.heroinfo_set.all()
    context = {'heros':heros}
    return render(request,"booktest/hero.html",context)