from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse("hello, world")
    return render(request, "hello/index.html")

def alkis(request):
    return HttpResponse("hello alkis")

def greet(request, name):
    #return HttpResponse(f"hello, {name.capitalize()}")
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })




