from pyexpat import model
from rest_framework import serializers

from catalogue.models import Book, BookImage, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id','first_name', 'last_name','email', 'dob']


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=True, read_only=True)
    images = serializers.HyperlinkedRelatedField(
        view_name='book-image-detail',
        queryset=BookImage.objects.all(),
        many=True
    )
    class Meta:
        model = Book
        fields = ("id" ,"title", "summary","images","author")

class AddBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','title','isbn','summary' ]


class BookImageSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        book_id = self.context['book_id']
        return BookImage.objects.create(book_id=book_id, **validated_data)

    class Meta:
        model = BookImage
        fields = ['id','image']


    # id = serializers.IntegerField()
    # title = serializers.CharField(max_length=255)
    # summary = serializers.CharField(max_length=255)