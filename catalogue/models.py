from django.db import models

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



class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    email = models.EmailField()



class Book(models.Model):
    title = models.CharField(max_length=255)
    author = ""
    summary = models.TextField()
    isbn = models.CharField(max_length=13, unique=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


