from django.shortcuts import render

from django.http import HttpResponse
from .forms import UploadImageForm
from PIL import Image
import os.path

def fileUploaderView(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES, request.FILES)
        filename = request.POST['title']
        if form.is_valid():
            upload(request.FILES['file'], filename)
            return HttpResponse("<h2>Image uploaded successful!</h2>")
        else:
            return HttpResponse("<h2>Image uploaded not successful!</h2>")
    form = UploadImageForm()
    return render(request, 'imageUploader.html', {'form': form})

def upload(f, filename):
    ext = os.path.splitext(f.name)[1][1:]
    fname = filename + "." + ext
    file = open(fname, 'wb+')
    for chunk in f.chunks():
        file.write(chunk)



