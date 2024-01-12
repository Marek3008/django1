from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.renderProducts, name="renderProducts"),
    path('categories/', views.renderCategories, name="renderCategories"),
    path('customers/', views.renderCustomers, name="renderCustomers"),
    path('orders/', views.renderOrders, name="renderOrders")
]