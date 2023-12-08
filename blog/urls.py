from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.drawPosts, name="drawPosts"),
    path('authors/', views.drawAuthors, name="drawAuthors"),
    path('categories/', views.drawCategories, name="drawCategories")
]