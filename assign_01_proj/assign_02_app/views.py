from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from assign_01_app.models import Person

#  Exercise 1 : create 02 views
def index(request):
    response = HttpResponse()
    person_list = Person.objects.order_by('id')[:10]
    for p in person_list:
        output = ', '.join([str(p.id), p.name, str(p.age), p.address, p.mobile_number])
        response.write(output)
        response.write("<br>")
    return HttpResponse(response)

def detail(request, person_id):
    response = HttpResponse()
    p = Person.objects.get(id=person_id)
    output = '<br>'.join([str(p.id), p.name, str(p.age), p.address, p.mobile_number])
    response.write(output)
    return HttpResponse(response)

#  Exercise 2 : use templates

class IndexView(generic.ListView):
    template_name = 'assign_02_app/index.html'
    context_object_name = 'person_list'

    def get_queryset(self):
        return Person.objects.all


class DetailView(generic.DetailView):
    model = Person
    template_name = 'assign_02_app/detail.html'


