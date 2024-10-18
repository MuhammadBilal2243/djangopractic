from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("this home")

# Create your views here.
