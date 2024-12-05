from django.shortcuts import render
from django.http import HttpRequest
from .models import Person

# Create your views here.
def index(request: HttpRequest):
    context = request.GET
    context.update({
        'people': Person.objects.all()
    })  
    return render(request, 'index.html', context)