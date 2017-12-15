from django.shortcuts import render
from django.db.models import F, Q, Sum, Count
from area.models import AeraInfo
from django.http import HttpResponse, JsonResponse


# Create your views here.
def area(request):
    dict = request.GET
    Aname = dict.get('n')
    are = AeraInfo.objects.get(aname=Aname)
    print(are.aparent)
    if are.aparent == None:
        parent = ""
    else:
        parent = are.aparent.aname
    son = are.aerainfo_set.all()
    list = []
    for i in son:
        list.append({"aname": i.aname})
    context = {"son": list, "parent": parent}
    return JsonResponse({"context": context})

    # return HttpResponse('{"name":"tom"}')


def index(request):
    return render(request, 'aera/aera.html')
