from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'isbn' )
    list_filter = ('isbn',)
    search_fields =('title',)

@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(models.Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(models.BookImage)
class BookImageAdmin(admin.ModelAdmin):
    list_display = ['book', 'image']
    list_display_links = ["image"]

