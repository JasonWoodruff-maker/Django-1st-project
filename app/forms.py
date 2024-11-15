from django import forms
from app.models import *


class recipe(forms.Form):
   name = forms.CharField()
   ingr = forms.CharField()
   Desc = forms.CharField()

