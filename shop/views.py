from django.shortcuts import render
from . models import *

def renderProducts(request):
    products = Product.objects.all()
    return render(request, "shop/index.html", {"products" : products})

def renderCategories(request):
    categories = Category.objects.all()
    return render(request, "shop/index.html", {"categories" : categories})

def renderCustomers(request):
    customers = Customer.objects.all()
    return render(request, "shop/index.html", {"customers" : customers})

def renderOrders(request):
    orders = Order.objects.all()
    return render(request, "shop/index.html", {"orders" : orders})


