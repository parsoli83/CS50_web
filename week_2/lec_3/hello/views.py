from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, "hello/index.html",{
        "username" : "parsa"
    })
def parsa(request):
    return HttpResponse("hello,parsa")
def greet(request, name):
    return HttpResponse(f"hello {name.upper()}")