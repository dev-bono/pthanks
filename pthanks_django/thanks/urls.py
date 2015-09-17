from django.conf.urls import include, url
from thanks.views import IndexView, LoginView

from . import views

urlpatterns = [
	# ex: /thanks/
	url(r'^$', IndexView.as_view(), name='index'),
	url(r'^login$', LoginView.as_view(), name='login'),
	# # ex: /thanks/5/
	# url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
	# # ex: /polls/5/results/
	# url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
	# # ex: /polls/5/vote/
	# url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
