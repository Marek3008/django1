from openpyxl import load_workbook
import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from skola.models import Student
import random

wb = load_workbook(filename="ULICE.xlsx")
ws = wb.active

adresy = list(ws.values)

studenti = Student.objects.all()

for student in studenti:
    adresa = random.choice(adresy)
    student.psc = adresa[2]
    student.obec = adresa[6]
    student.ulica = adresa[1]
    student.cislo_domu = random.choice([1,2,3,4,5,6,7,8,9,10])
    student.save()