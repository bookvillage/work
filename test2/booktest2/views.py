from django.shortcuts import render
from django.http import HttpResponse
from booktest2.models import BookInfo, HeroInfo
from django.db.models import F, Q, Max, Avg, Min, Count, Sum


# Create your views here.
def index(request):
    return HttpResponse("你好歹")


def booklist(request):
    books = BookInfo.objects.all()
    list1 = BookInfo.objects.filter(id=1)
    list2 = BookInfo.objects.filter(btitle__contains="传")
    list3 = BookInfo.objects.filter(btitle__endswith="部")
    list4 = BookInfo.objects.filter(btitle__startswith="天")
    list5 = BookInfo.objects.filter(bremack__isnull=False)
    list6 = BookInfo.objects.filter(id__in=[1, 3, 4])
    list7 = BookInfo.objects.filter(id__lte=3)
    list8 = BookInfo.objects.filter(bpub_date__year=1980)
    list9 = BookInfo.objects.exclude(id__in=[1, 4])
    list10 = BookInfo.objects.filter(bread__gte=F('bcommet'))  # 比较运算符
    list11 = BookInfo.objects.filter(~Q(bread__gte=F('bcommet')) & Q(bremack__isnull=False))  # 逻辑运算符&,|,~
    list12 = BookInfo.objects.filter(bread__gte=30).order_by('-bread')
    list13 = BookInfo.objects.aggregate(Sum('bread'))
    list14 = BookInfo.objects.exclude(heroinfo__hcontent__contains="八")
    context = {
        'books': books,
        'list1': list1,
        'list2': list2,
        'list3': list3,
        'list4': list4,
        'list5': list5,
        'list6': list6,
        'list7': list7,
        'list8': list8,
        'list9': list9,
        'list10': list10,
        'list11': list11,
        'list12': list12,
        'list13': list13,
        'list14': list14
    }
    return render(request, 'booktest2/booklist.html', context)


