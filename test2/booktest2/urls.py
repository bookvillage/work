from django.conf.urls import include, url
from booktest2 import views

urlpatterns = [
    url(r'^index',views.index),
    url(r'^booklist', views.booklist),

]
