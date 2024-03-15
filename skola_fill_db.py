import os, django, random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from skola.models import *

triedy = []

for rocnik in range(1, 5):
    for pismenko in ['A', 'B', 'C', 'D']:
        triedy.append(f"{rocnik}.{pismenko}")
        Trieda.objects.create(nazov=f"{rocnik}.{pismenko}")


fileMena = open("mena.txt", 'r', encoding="utf-8")
mena = fileMena.read().splitlines()

filePriezviska = open("priezviska.txt", 'r', encoding="utf-8")
priezviska = filePriezviska.read().splitlines()


for i in range(20):
    meno = random.choice(mena)
    priezvisko = random.choice(priezviska)
    titul = random.choice(["Ing.", "PhDr.", "RnDr.", "Bc.", "Mgr.", "PaeDr.", ""])

    if i < len(triedy):
        trieda = Trieda.objects.get(nazov=triedy[i])
        Ucitel.objects.create(meno=meno, priezvisko=priezvisko, trieda=trieda)

    else:
        Ucitel.objects.create(titul=titul, meno=meno, priezvisko=priezvisko)


for i in range(100):
    meno = random.choice(mena)
    priezvisko = random.choice(priezviska)
    trieda = Trieda.objects.get(nazov=random.choice(triedy))
    Student.objects.create(meno=meno, priezvisko=priezvisko, trieda=trieda)