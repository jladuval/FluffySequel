__author__ = 'Jacob'
from django import forms

class FluffyForm(forms.Form):
    courseLink = forms.CharField(max_length=500)