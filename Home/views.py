from random import randint
import datetime
from django.db import transaction
from django.db.models import Count
from django.shortcuts import render_to_response
from django.template import RequestContext
from Home.forms import FluffyForm
from Home.models import CoarseLink, FluffyLink

__author__ = 'Jacob'


def index(request):
    if request.method == 'POST':
        form = FluffyForm(request.POST)
        if form.is_valid():
            fluffyLink = __GetFluffyLink(form.courseLink)
            return render_to_response('Home/fluffyLink.html', {'FluffyLink': fluffyLink.text }, context_instance=RequestContext(request))
    else:
        formModel = FluffyForm()
    return render_to_response('Home/index.html', {"form" : formModel}, context_instance=RequestContext(request))

def __GetFluffyLink(coarseLink):
    link = CoarseLink.objects.get(text=coarseLink)
    if(link == None):
        link = __CreateNewCoarseLink(coarseLink)

    return link

@transaction.commit_on_success
def __CreateNewCoarseLink(coarseLink):
    link = FluffyLink.objects.filter(lastAccessed=None)
    count = link.aggregate(count=Count('id'))['count']
    random_index = randint(0, count - 1)
    link = FluffyLink.objects.all()[random_index]
    link.lastAccessed = datetime.datetime.now()
    newCoarseLink = CoarseLink(text = coarseLink, FluffyLink = link)
    return newCoarseLink