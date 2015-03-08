from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from harmas import Harmas
import json
def index(request):
	h = Harmas()
	idopontok = h.idopontok()
	kovetkezo = h.kovetkezo_erkezes()
	return render(request,'harmasbusz/index.html',{
		"idopontok": idopontok,
		"kovetkezo_p": kovetkezo[0],
		"kovetkezo_m": kovetkezo[1]
	})
def update(request):
	h = Harmas()
	kovetkezo = h.kovetkezo_erkezes()
	json_data = json.dumps(kovetkezo)
	return HttpResponse(json_data)