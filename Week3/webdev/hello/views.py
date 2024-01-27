from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def eizad(request):
    return HttpResponse("Hello, Eizad!")

def hamdan(request):
    return HttpResponse("Hello, Eizad Hamdan!")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })
