import os, django, datetime, random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from skola.models import Student, Ucitel

studenti = Student.objects.all()
ucitelia = Ucitel.objects.all()

def getVek(trieda, ucitel = 0):
    if ucitel == 0:
        if trieda[0] == '1':
            return 16
        elif trieda[0] == '2':
            return 17
        elif trieda[0] == '3':
            return 18
        elif trieda[0] == '4':
            return 19
    
    else:
        return random.randint(26, 70)
    


def getDate(vek):
    dnes = datetime.datetime.today()
    zaciatok = datetime.date(dnes.year - vek, 1, 1)
    konec = datetime.date(dnes.year - vek, 12, 31)
    pocet = (konec - zaciatok).days
    random_den = random.randint(1, pocet)
    random_datum = zaciatok + datetime.timedelta(days=random_den)
    return random_datum

for student in studenti:
    trieda = student.trieda.nazov
    vek = getVek(trieda)
    student.datum_narodenia = getDate(vek)
    student.save()

for ucitel in ucitelia:
    trieda = student.trieda.nazov
    vek = getVek(trieda, 1)
    ucitel.datum_narodenia = getDate(vek)
    ucitel.save()
