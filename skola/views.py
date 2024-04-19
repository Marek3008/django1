from django.shortcuts import render, HttpResponse
from . models import *

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

    print(studentList)
    print(trieda)

    ucitel = Ucitel.objects.get(trieda_id=triedaObj.pk)
    ucitel = f"{ucitel.titul} {ucitel.meno} {ucitel.priezvisko}"

    return render(request, "skola/trieda.html", {"trieda" : trieda, "ucitel" : ucitel, "studenti" : studentList})

def vypisOStudentoviPodlaTriedy(request, student):
    meno = str(student).split()[0]
    priezvisko = str(student).split()[1]
    
    
    studentObj = Student.objects.get(meno=meno, priezvisko=priezvisko)
    kruzky = Kruzok.objects.filter(student=studentObj.pk)

    return render(request, "skola/student.html", {"student" : student, "kruzky" : kruzky})

def vypisOUciteloviPodlaTriedy(request, ucitel):
    meno = str(ucitel).split()[-2]
    priezvisko = str(ucitel).split()[-1]

    print(meno)
    print(priezvisko)

    ucitel = Ucitel.objects.get(meno=meno, priezvisko=priezvisko)

    return render(request, "skola/ucitel.html", {"ucitel" : ucitel})

def vypisKruzky(request):
    kruzky = Kruzok.objects.all()

    return render(request, "skola/kruzky.html", {"kruzky" : kruzky})

def vypisKruzok(request, kruzok):
    kruzokObj = Kruzok.objects.get(nazov=kruzok)
    studenti = Student.objects.filter(kruzok=kruzokObj.pk)
    ucitel = kruzokObj.ucitel

    return render(request, "skola/kruzok.html", {"kruzok" : kruzokObj, "studenti" : studenti, "ucitel" : ucitel})