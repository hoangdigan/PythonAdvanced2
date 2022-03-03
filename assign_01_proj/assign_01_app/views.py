from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    response = HttpResponse()
    response.write("<h1> WELCOME</h1>")
    response.write("This is my first Django application")
    return response



