from django import forms
from django.forms import ModelForm
from .models import *

class itemForm(forms.ModelForm):

    class Meta:
        model = item
        fields = '__all__'




