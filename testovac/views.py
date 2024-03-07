from django.shortcuts import render
from kalkulacka.models import Priklad
import random

def renderEquation(request):
    global spravnyVysledok

    if request.method == "GET":
        priklady = Priklad.objects.all()
        
        priklad = random.choice(priklady)

        a = priklad.a
        b = priklad.b
        operator = priklad.operator
        spravnyVysledok = priklad.vysledok

        return render(request, "testovac/index.html", {"a" : a, "b" : b, "operator" : operator})
    
    else:      
        try:
            vysledok = float(request.POST["vysledok"])
        except ValueError:
            problem = True
            return render(request, "testovac/index.html", {"problem" : problem})

        if vysledok == spravnyVysledok:
            spravnost = True
        else:
            spravnost = False

        
        return render(request, "testovac/index.html", {"spravnost" : spravnost})
        


        

    
   