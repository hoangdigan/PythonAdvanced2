from django import forms
from django.forms import ModelForm
from .models import Animal

class AnimalForm(ModelForm):
    class Meta:
        model = Animal
        fields = ['id', 'name', 'age', 'color']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'})
        }


