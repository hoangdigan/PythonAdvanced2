from django import forms

class UploadImageForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.ImageField()

    widgets = {
        'tilte': forms.TextInput(attrs={'class': 'form-control'}),
        'file': forms.TextInput(attrs={'class': 'form-control'})
    }

