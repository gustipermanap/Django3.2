from django.shortcuts import render
from django.http import HttpResponse

def index(response, id):
	return HttpResponse("<h1>%s</h1>" % id)

