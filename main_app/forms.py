from django.forms import ModelForm
from .models import Mod

class ModForm(ModelForm):
    class Meta():
        model = Mod
        fields = ['part', 'use']