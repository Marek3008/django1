from django.db import models


class Trieda(models.Model):

    nazov = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.nazov}"
    
    class Meta:
        verbose_name = "Trieda"
        verbose_name_plural = "Triedy"
        ordering = ["nazov"]

class Ucitel(models.Model):

    titul = models.CharField(max_length=20)
    meno = models.CharField(max_length=20)
    priezvisko = models.CharField(max_length=20)
    trieda = models.ForeignKey(Trieda, on_delete=models.SET_NULL, null=True, blank=True)
    datum_narodenia = models.DateField(null=True)

    def __str__(self):
        if self.trieda:
            return f"{self.titul} {self.meno} {self.priezvisko}"
        
        else:
            return f"{self.titul} {self.meno} {self.priezvisko}"
        
    class Meta:
        verbose_name = "Učiteľ"
        verbose_name_plural = "Učitelia"
        ordering = ["priezvisko"]
        
class Kruzok(models.Model):

    nazov = models.CharField(max_length=50)
    skratka = models.CharField(max_length=5)
    ucitel = models.ForeignKey(Ucitel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nazov}"
    
    class Meta:
        verbose_name = "Krúžok"
        verbose_name_plural = "Krúžky"
        ordering = ["nazov"]
    
class Student(models.Model):

    meno = models.CharField(max_length=20)
    priezvisko = models.CharField(max_length=20)
    trieda = models.ForeignKey(Trieda, on_delete=models.SET_NULL, null=True, blank=True)
    kruzok = models.ManyToManyField(Kruzok, blank=True)
    datum_narodenia = models.DateField(null=True)
    psc = models.CharField(max_length=6, null=True)
    ulica = models.CharField(max_length=20, null=True)
    cislo_domu = models.IntegerField(null=True)
    obec = models.CharField(max_length=20, null=True)
    

    def __str__(self):
        return f"{self.meno} {self.priezvisko} {self.trieda}"
    
    class Meta:
        verbose_name = "Študent"
        verbose_name_plural = "Študenti"
        ordering = ["priezvisko"]

class PokusnyKralik(models.Model):
    
    meno = models.CharField(max_length=20)
    priezvisko = models.CharField(max_length=20)
    email = models.EmailField()
    datum = models.DateField()

    def __str__(self):
        return f"{self.meno} {self.priezvisko}"
    
    class Meta:
        verbose_name = "Pokusný králik"
        verbose_name_plural = "Pokusné králiky"
        ordering = ["priezvisko", "meno"]