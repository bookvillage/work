from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def book(request):
    return HttpResponse("<h1>书店<h1>")

def photo(request):
    return render(request,'bookvillage/photo.html')