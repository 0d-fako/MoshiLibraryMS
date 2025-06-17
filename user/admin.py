from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models

# Register your models here.
@admin.register(models.Author)
class AuthorAdmin(UserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "usable_password", "password1", "password2","first_name","last_name","email","phone_number","dob" ),
            },
        ),
    )