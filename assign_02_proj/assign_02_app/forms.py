from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Person
        fields = "__all__"
