from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = ""
    summary = models.TextField()
    isbn = models.CharField(max_length=13, unique=True)
    genre = ""



