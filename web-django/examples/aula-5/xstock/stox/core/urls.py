from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^item/(?P<pk>[0-9]+)/$', views.item_detail, name='item_detail'),
]
