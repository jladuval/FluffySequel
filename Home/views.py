from django.shortcuts import render_to_response
from django.template import RequestContext
from Home.forms import FluffyForm

__author__ = 'Jacob'


def index(request):
    if request.method == 'POST':
        form = FluffyForm(request.POST)
        if form.is_valid():
            return render_to_response('Home/fluffyLink.html')
    else:
        formModel = FluffyForm()
    return render_to_response('Home/index.html', {"form" : formModel}, context_instance=RequestContext(request))