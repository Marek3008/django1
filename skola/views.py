from django.shortcuts import render, HttpResponse
from . models import Student, Ucitel, Trieda

def vypisSkola(request):
    studenti = Student.objects.all().order_by("priezvisko")
    ucitelia = Ucitel.objects.all().order_by("priezvisko")
    triedy = Trieda.objects.all().order_by("nazov")

    return render(request, "skola/index.html", {"studenti" : studenti, "ucitelia" : ucitelia, "triedy" : triedy})

def vypisStudent(request):
    studenti = Student.objects.all()
    return render(request, "skola/index.html", {"studenti" : studenti})

def vypisTriedy(request):
    triedy = Trieda.objects.all()
    return render(request, "skola/index.html", {"triedy" : triedy})

def vypisUcitel(request):
    ucitelia = Ucitel.objects.all()
    return render(request, "skola/index.html", {"ucitelia" : ucitelia})