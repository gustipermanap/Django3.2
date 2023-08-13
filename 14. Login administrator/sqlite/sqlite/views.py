from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("<h1>Text Di Index</h1>")

def v1(request):
	return HttpResponse("<h1>View 1!</h1>")

