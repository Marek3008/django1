from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.vypisSkola, name='vypisSkola'),
    path('triedy/', views.vypisTriedy, name="vypisTriedy"),
    path('studenti/', views.vypisStudent, name="vypisStudent"),
    path('ucitelia/', views.vypisUcitel, name="vypisUcitel"),
    path('triedy/<trieda>/', views.vypisTrieda, name="vypisTrieda")
]
