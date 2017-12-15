from django.conf.urls import url
from booktest import views


urlpatterns = [
    url(r'index',views.index),
    url(r'get',views.get),
    url(r'wish$',views.wish),
    url(r'wishs',views.wishs),
    url(r'post',views.post)
]
