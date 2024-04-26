from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.vypisSkola, name='vypisSkola'),
    path('triedy/', views.vypisTriedy, name="vypisTriedy"),
    path('studenti/', views.vypisStudent, name="vypisStudent"),
    path('ucitelia/', views.vypisUcitel, name="vypisUcitel"),
    path('triedy/<trieda>/', views.vypisTrieda, name="vypisTrieda"),
    path('studenti/<student>/', views.vypisOStudentoviPodlaTriedy, name="vypisOStudentoviPodlaTriedy"),
    path('ucitelia/<ucitel>', views.vypisOUciteloviPodlaTriedy, name="vypisOUciteloviPodlaTriedy"),
    path('kruzky/', views.vypisKruzky, name="vypisKruzky"),
    path('kruzky/<kruzok>', views.vypisKruzok, name="vypisKruzok"),
    path('uzivatel-pridaj/', views.pridajPouzivatel, name="pridajPouzivatel"),
]
