# import form class from django
from assign_01_app.models import Person
from django import forms

# create a ModelForm
class PersonForm(forms.ModelForm):
	# specify the name of model to use
	class Meta:
		model = Person
		fields = "__all__"
