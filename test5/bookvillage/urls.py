from django.conf.urls import url
from bookvillage import views

urlpatterns = [
    url(r'^village', views.book),
    url(r'^photo',views.photo)
]
