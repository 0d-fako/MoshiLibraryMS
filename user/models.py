from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=11, unique=True)





class Author(User):
    dob = models.DateField(blank=False, null=False)
    dod = models.DateField(blank=False, null=True)