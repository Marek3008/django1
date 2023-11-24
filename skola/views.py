from django.shortcuts import render, HttpResponse
from . models import Student, Ucitel

def vypisStudent(request):
    studenti = Student.objects.all()
    return (HttpResponse(studenti))