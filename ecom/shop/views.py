from django.shortcuts import render
from  django.http import  HttpResponse
from .models import product
from math import  ceil
def index(request):
    products = product.objects.all()
    print(products)
    n=len(products)
    no_slides=(n//4)+ceil((n/4)-(n//4))
    parems={'product':products,'no_of_slides':no_slides,'range':range(1,no_slides)}

    return  render(request,'shop/index.html',parems)
def contect(request):
    return  HttpResponse("this my contect")
def about(request):
    return  render(request,'shop/about.html')
def search(request):
    return  HttpResponse("this my search")
def prodview(request):
    return  HttpResponse("this my prodview")
def checkout(request):
    return  HttpResponse("this my checkout")
