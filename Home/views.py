from random import randint
import datetime
import uuid
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
            coarseLink = form.cleaned_data['coarseLink']
            fluffyLink = __GetFluffyLink(coarseLink)
            return render_to_response('Home/fluffyLink.html', {'FluffyLink': fluffyLink }, context_instance=RequestContext(request))
    else:
        formModel = FluffyForm()
    return render_to_response('Home/index.html', {"form" : formModel}, context_instance=RequestContext(request))

def __GetFluffyLink(coarseLink):
    try:
        link = CoarseLink.objects.get(text=coarseLink)
    except CoarseLink.DoesNotExist:
        link = __CreateNewCoarseLink(coarseLink)

    return link.fluffyLink.text

@transaction.commit_on_success
def __CreateNewCoarseLink(coarseLink):
    link = FluffyLink.objects.filter(lastAccessed=None)
    count = link.aggregate(count=Count('id'))['count']
    if count == 0:
        link = FluffyLink(text = uuid.uuid1(), lastAccessed = datetime.datetime.now())
        newCoarseLink = CoarseLink(text = coarseLink, fluffyLink = link)
    else:
        random_index = randint(0, count - 1)
        link = FluffyLink.objects.all()[random_index]
        link.lastAccessed = datetime.datetime.now()
        newCoarseLink = CoarseLink(text = coarseLink, FluffyLink = link)
    return newCoarseLink