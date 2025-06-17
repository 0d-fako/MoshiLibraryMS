from pyexpat import model
from rest_framework import serializers

from catalogue.models import Book
from user.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name']


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=True, read_only=True)
    class Meta:
        model = Book
        fields = ("id" ,"title", "summary","author")



    # id = serializers.IntegerField()
    # title = serializers.CharField(max_length=255)
    # summary = serializers.CharField(max_length=255)