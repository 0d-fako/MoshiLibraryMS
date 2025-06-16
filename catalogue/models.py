import uuid

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Genre(models.Model):
    GENRE_CHOICES = (
        ("ROMANCE", "R"),
        ("COMEDY", "C"),
        ("FINANCE", "F"),
        ("POLITICS", "P"),
    )
    name = models.CharField(max_length=10, choices=GENRE_CHOICES, default="R")

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    email = models.EmailField()



class Book(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField()
    isbn = models.CharField(max_length=13, unique=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class BookInstance(models.Model):
    LOAN_STATUS = (
        ("A", "AVAILABLE"),
        ("B","BORROWED"),
        ("M", "MAINTENANCE"),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=LOAN_STATUS, default="A")
    return_date = models.DateTimeField(blank=False, null=False)
    comments=models.TextField(blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)