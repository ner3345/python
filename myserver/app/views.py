from django.shortcuts import render_to_response
from django.http import HttpResponse
# Create your views here.


def index(request):
	return render_to_response('index.html',{'name':'liuhuawei'})
	# return HttpResponse("Hello World")