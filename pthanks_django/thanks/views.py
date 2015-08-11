from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from thanks.models import Thanks


def index(request):
	latest_thanks_list = Thanks.objects.order_by('-create_dt')[:5]
	context = {
		'latest_thanks_list': latest_thanks_list,
	}
	return render(request, 'thanks/index.html', context)
