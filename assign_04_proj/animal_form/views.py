from django.shortcuts import render
from django.http import HttpResponse
from .forms import AnimalForm
from . import forms

def addform(request):
    # context = {}
    form = forms.AnimalForm()
    if request.method == 'POST':
        form = AnimalForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            # save the form data to model
            form.save()
            message = 'Update Successfully. Thank you!'
            return render(request, "index.html")
        else:
            message = 'Data is invalid, try again!'
    else:
        message = 'Input your information!'
    # context['form'] = form
    return render(request, "add_animal.html", {'message': message, 'form': form})