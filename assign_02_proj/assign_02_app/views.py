from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Person
from .forms import PersonForm

#  Exercise 1 : use view

class IndexView(generic.ListView):
    template_name = 'assign_02_app/index0.html'
    context_object_name = 'person_list'

    def get_queryset(self):
        return Person.objects.all()

class DetailView(generic.DetailView):
    model = Person
    template_name = 'assign_02_app/detail.html'

#  Exercise 2 : use teamplate
def index(request):
    person_list = Person.objects.order_by('id')[:10]
    context = {'person_list': person_list}
    return render(request, 'assign_02_app/index0.html', context)

def detail(request, person_id):
    try:
        person = Person.objects.get(pk=person_id)
    except Person.DoesNotExist:
        raise Http404("Person does not exist")
    return render(request, 'assign_02_app/detail.html', {'person': person})

# excercise 3 : form
def formInput(request):
    context = {}

    # create object of form
    form = PersonForm(request.POST or None, request.FILES or None)

    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()

    context['form'] = form
    return render(request, "assign_02_app/form.html", context)

