from django.test import TestCase
from . import views
from django.conf.urls import include, url

urlpatterns = [
               #url(r'^ml/(?P<str>\w+)/$/', views.process_detail, name='process_detail'),
               #url(r'^ml/', views.process_detail, name='process_detail'),
               url(r'^ml/([\w ]+)/$', views.process_detail, name='process_detail'),
               #url(r'^utils/$', views.process_detail, name='process_detail'),
               #url(r'^([\w ]+)/$', views.process_detail, name='process_detail'),
               ]
