from django.db import models
from django.utils import timezone

class Category(models.Model):

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Product(models.Model):

    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=7)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.price}€"
    
class Customer(models.Model):

    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.name} {self.surname}"
    
class Order(models.Model):

    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    create_Date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Customer: {self.customer}; Product: {self.product}"
