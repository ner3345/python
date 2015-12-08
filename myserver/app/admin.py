#-*-coding:utf8-*-
from django.contrib import admin
from django.shortcuts import render_to_response
from django.http import HttpResponse
# Register your models here.

def index(request):
	return render_to_response('index.html',{'name':'这是后台'})
