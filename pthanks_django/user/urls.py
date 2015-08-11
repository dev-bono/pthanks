from django.conf.urls import include, url

from user import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
]
