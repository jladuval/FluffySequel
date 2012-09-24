__author__ = 'Jacob'
from django.db import models

class Adjective(models.Model) :
    text = models.TextField()

class Noun(models.Model) :
    text = models.TextField()

class FluffyLink(models.Model) :
    text = models.TextField()
    lastAccessed = models.DateTimeField()

class CoarseLink(models.Model):
    text = models.TextField()
    fluffyLink = models.ForeignKey(FluffyLink)

