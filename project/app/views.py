from django.shortcuts import render
from django.http import HttpRequest
from .models import Person

# Create your views here.
def index(request: HttpRequest):
    context = request.GET.__dict__
    context.update({
        'people': Person.objects.all()
    })
    newPerson = Person(("".join([person.name for person in Person.objects.all()])), sum([i.age for i in Person.objects.all()]))
    newPerson.save()
    return render(request, 'index.html', context)