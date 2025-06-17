from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from . import models

# Register your models here.


@admin.register(models.User)
class UserAdmin(BaseUserAdmin):
    pass




@admin.register(models.Author)
class AuthorAdmin(BaseUserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "usable_password", "password1", "password2","first_name","last_name","email","phone_number","dob" ),
            },
        ),
    )
    list_display = ("first_name","last_name","email","phone_number","dob","dod" )
    list_display_links = ("email","phone_number","dod" )
    list_editable = ("first_name","last_name","phone_number")
    list_per_page = 10