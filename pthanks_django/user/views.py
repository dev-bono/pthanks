from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
	#latest_thanks_list = Thanks.objects.order_by('-create_dt')[:5]
	#output = ', '.join([p.question_text for p in latest_thanks_list])
	return HttpResponse("USER LIST")