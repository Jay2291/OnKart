from math import ceil
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def index(request):
    products= Product.objects.all()
    n = len(products)
    nSlides = n//4 + ceil((n/4)-(n//4))
    allProds =[[products, range(1, nSlides), nSlides],
               [products, range(1, nSlides), nSlides]]
    params = {'allProds':allProds }
    return render(request,"shop/index.html", params)


def about(request):
    return render(request, "shop/about.html")

def contact(request):
    return HttpResponse("contact")

def tracker(request):
    return HttpResponse("tracker")

def search(request):
    return HttpResponse("search")

def product(request):
    return HttpResponse("product")

def checkout(request):
    return HttpResponse("CHeckout")
