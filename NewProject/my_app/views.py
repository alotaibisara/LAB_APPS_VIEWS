from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.



def index(request : HttpRequest):

    result = "Hello World, This is my new HOME !"

    return HttpResponse(result)

def aboutfunction(request: HttpRequest):
  
    result = "A simple paragraph about the website."
  
    return HttpResponse (result)
