from django.db import models
from django.utils import timezone

class Author(models.Model):

    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    nickname = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.name} {self.surname} ({self.nickname})"
    
class Category(models.Model):

    name = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.name}"

class Post(models.Model):

    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True)
    create_Date = models.DateTimeField(default=timezone.now)
    publish_Date = models.DateTimeField(default=timezone.now)
    text = models.TextField()
    heading = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Author: {self.author} Date of creation: {self.create_Date} Date of publication: {self.publish_Date} Heading: {self.heading} Category: {self.category}"
