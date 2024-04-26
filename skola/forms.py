from django import forms
from . models import PokusnyKralik

class PokusnyKralikForm(forms.ModelForm):
    class Meta:
        model = PokusnyKralik
        fields = "__all__"