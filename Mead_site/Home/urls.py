from django.conf.urls import url, include
from . import views

urlpatterns = [
	url('contact/', views.contact, name='contact'),
	url(r'^$', views.index, name='index'),
	]