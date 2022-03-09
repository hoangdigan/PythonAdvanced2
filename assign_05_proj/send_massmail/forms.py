from django import forms


class EmailForm(forms.Form):
    email = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 25, 'placeholder': 'Send many mail, use (;) please'}))
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 25}))
    attach = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)