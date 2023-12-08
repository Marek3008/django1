from django.shortcuts import render
from . models import *

posts = Post.objects.all()
authors = Author.objects.all()
categories = Category.objects.all()

def drawPosts(request):
    return render(request, "blog/index.html", {"posts" : posts})

def drawAuthors(request):
    return render(request, "blog/index.html", {"authors" : authors})

def drawCategories(request):
    return render(request, "blog/index.html", {"categories" : categories})
