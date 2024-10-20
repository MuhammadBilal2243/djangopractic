from django.shortcuts import render
from  django.http import  HttpResponse
def index(request):
    return  render(request,'shop/index.html')
def contect(request):
    return  HttpResponse("this my contect")
def about(request):
    return  HttpResponse("this my about")
def search(request):
    return  HttpResponse("this my search")
def prodview(request):
    return  HttpResponse("this my prodview")
def checkout(request):
    return  HttpResponse("this my checkout")
