from django import forms
from .models import *

class ImageForm(forms.Form):
    img = forms.ImageField()