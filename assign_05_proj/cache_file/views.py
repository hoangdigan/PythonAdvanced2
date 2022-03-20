from django.shortcuts import render
from django.http import HttpResponse

def SampleView(request):
    html = '<h1>Django Caching<h1><br><p>Welcome to Caching Tutorial</p>'
    return HttpResponse(html)