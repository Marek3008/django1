from django.shortcuts import render, HttpResponse
from . models import *

def renderCalc(request):
    if request.method == "GET":
        return render(request, "kalkulacka/index.html")
    else:
        try:
            a = float(request.POST["a"])
            b = float(request.POST["b"])

        except:
            vysledok = "nespravny input"
            return render(request, "kalkulacka/index.html", {"vysledok" : vysledok})
        
        operator = request.POST["operator"]
        
        if operator == "+":
            vysledok = a + b
        elif operator == "-":
            vysledok = a - b
        elif operator == "*":
            vysledok = a * b
        elif operator == "/":
            try:        
                vysledok = a / b
            except:
                vysledok = "nemozes delit nulou"
                return render(request, "kalkulacka/index.html", {"vysledok" : vysledok})
        
        try:
            priklad_check = Priklad.objects.get(a=a, b=b, operator=operator)
        except:
            priklad = Priklad(
                a = a,
                b = b,
                operator = operator,
                vysledok = vysledok
            )
            priklad.save()
        
        return render(request, "kalkulacka/index.html", {"vysledok" : vysledok, "a" : a, "b" : b, "operator" : operator})

