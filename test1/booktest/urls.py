from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'index4343',views.index),
    url(r'index1',views.index1),
    url(r'hero/(\d+)$',views.index2)
]