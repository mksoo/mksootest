from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("myapp index")


def about(request):
    return HttpResponse("About page")

def h2(request):
    return HttpResponse("<h2>h2 man</h2>")