from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView

# Create your views here.
from thanks.models import Thanks

class IndexView(ListView):
	context_object_name = 'latest_thanks_list'
	queryset = Thanks.objects.order_by('-create_dt')[:5]
	template_name = "thanks/index.html"

	# def get_context_data(self, **kwargs):
	# 	context = super(IndexView, self).get_context_data(**kwargs)
	# 	context['latest_thanks_list'] = Thanks.objects.order_by('-create_dt')[:5]
	# 	return context



# def index(request):
# 	latest_thanks_list = Thanks.objects.order_by('-create_dt')[:5]
# 	context = {
# 		'latest_thanks_list': latest_thanks_list,
# 	}
# 	return render(request, 'thanks/index.html', context)
