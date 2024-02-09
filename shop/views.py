from django.shortcuts import render
from . models import *

categories = Category.objects.all()

def renderProducts(request):
    products = Product.objects.all()
    return render(request, "shop/index.html", {"products" : products, "categories" : categories})

def renderCategories(request):
    categories = Category.objects.all()
    return render(request, "shop/index.html", {"categories" : categories})

def renderCustomers(request):
    customers = Customer.objects.all()
    return render(request, "shop/index.html", {"customers" : customers})

def renderOrders(request):
    orders = Order.objects.all()
    return render(request, "shop/index.html", {"orders" : orders})

def renderCategory(request, kategoria):
    kategoriaObj = Category.objects.get(name=kategoria)
    produkty = Product.objects.filter(category_id=kategoriaObj.pk)

    produktyList = []
    for produkt in produkty:
        produktyList.append(produkt)

    return render(request, "shop/category.html", {"produkty" : produkty})

