from django.shortcuts import render
#coding:utf-8
# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse(u'欢迎来到刘祥麟的个人站点')