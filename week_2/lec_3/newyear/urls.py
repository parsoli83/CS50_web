from django.urls import path
from . import views
# because they are located in the same directory


urlpatterns =[
    path("", views.index, name="index"), 
]