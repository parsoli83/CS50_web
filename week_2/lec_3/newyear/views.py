from django.shortcuts import render
from random import randint
# Create your views here.

def index(request):
    return render(request,"newyear/index.html",{
        "phrase": "parsa",
        "n" : 12
    })