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
    name = models.CharField(max_length=10, choices=GENRE_CHOICES, default="R", unique=True )

    def __str__(self):
        return self.name

class Language(models.Model):
    LANG_CHOICES = (
        ("YORUBA", "Y"),
        ("ENGLISH", "E"),
        ("FRENCH", "F"),
    )
    name = models.CharField(max_length=10, choices=LANG_CHOICES, default="Y", unique=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    email = models.EmailField()

    def __str__(self):
        return f'self.first_name + self.last_name'


class Book(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField()
    isbn = models.CharField(max_length=13, unique=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, default=1)
    author = models.ManyToManyField(Author, related_name="books")

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



class BookImage(models.Model):
    image = models.ImageField(upload_to="book/images", blank=True, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="images")

    def __str__(self):
        return self.image.url