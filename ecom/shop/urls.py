from django.urls import path
from . import  views
urlpatterns = [

    path("",views.index,name="shop"),
    path("contect/",views.contect,name="contect"),
    path("about/",views.about,name="about"),
    path("search/",views.search,name="search"),
    path("prodview",views.prodview,name="prodview"),
    path("checkout",views.checkout,name="checkout"),

]