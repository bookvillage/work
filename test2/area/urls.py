from django.conf.urls import include, url
from area import views

urlpatterns = [
    url(r'^areainq$',views.index),
    url(r'^areainq1', views.area)#(\?n=.*)?,

]