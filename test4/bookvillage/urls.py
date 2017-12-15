from django.conf.urls import url
from bookvillage import views

urlpatterns = [
    url(r'nihao', views.nihao),
    url(r'^setcookie$', views.setcookie),
    url(r'^getcookie$', views.getcookie),
    url(r'set_session$', views.set_session),
    url(r'get_session$', views.get_session),
    url(r'delsession$', views.delsession),
    url(r'bookprice$', views.bookprice, name='price'),
    url(r'^login$', views.login, name='login'),
    url(r'^verify$', views.verify),
    url(r'^login_check$', views.login_check),

]
