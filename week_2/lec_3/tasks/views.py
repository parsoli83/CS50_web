from django.shortcuts import render
from django import forms
# Create your views here.
tasks=[
    "a",
    "b",
    "c",
    "d",
    "e"
]

class new_email_form(forms.Form):
     task = forms.CharField(label="email")

def index(request):
     return render(request, "tasks/index.html", {
          "tasks":tasks
     })

def add(request):
     if request.method=="POST":
          form = new_email_form(request.POST)
          # you got the form
          if form.is_valid():
               email = form.cleaned_data["email"]
          else:
               return render(request, "tasks/add.html",{
                    "form": form,
                    "errors":"Invalid email"
               })
     return render(request, "tasks/add.html",{
          "email": new_email_form()
     })