from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.
def index(request: HttpRequest):
    context = request.GET
    return render(request, 'index.html', context)