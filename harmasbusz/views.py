from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from harmas import Harmas

def index(request):
	h = Harmas()
	harmas = h.get()
	return render(request,'harmasbusz/index.html',{ "harmas": harmas })