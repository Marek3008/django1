from django.shortcuts import render, HttpResponse
from . models import Student, Ucitel, Trieda

studenti = Student.objects.all().order_by("priezvisko")
ucitelia = Ucitel.objects.all().order_by("priezvisko")
triedy = Trieda.objects.all().order_by("nazov")


def vypisSkola(request):
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

def vypisTrieda(request, trieda):
    triedaObj = Trieda.objects.get(nazov=trieda)
    studenti = Student.objects.filter(trieda_id=triedaObj.pk).order_by("priezvisko")
    studentList = []
    for student in studenti:
        studentList.append(f"{student.meno} {student.priezvisko}")

    ucitel = Ucitel.objects.get(trieda_id=triedaObj.pk)
    ucitel = f"{ucitel.titul} {ucitel.meno} {ucitel.priezvisko}"

    return render(request, "skola/trieda.html", {"trieda" : trieda, "ucitel" : ucitel, "studenti" : studentList})
