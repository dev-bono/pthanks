from django.conf.urls import include, url

from . import views

urlpatterns = [
	# ex: /thanks/
	url(r'^$', views.index, name='index'),
	# # ex: /thanks/5/
	# url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
	# # ex: /polls/5/results/
	# url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
	# # ex: /polls/5/vote/
	# url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
