from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework import status, viewsets, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


from catalogue.models import Book, BookImage, Author, BookInstance
from catalogue.serializers import BookSerializer, AuthorSerializer, AddBookSerializer, BookImageSerializer, \
    BookInstanceSerializers


# Create your views here.

@api_view(['GET'])
def get_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


def greet(request, name):
    return render(request, 'index.html', {'name': name})


class AddAuthorView(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class GetUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

@api_view(['GET'])
def image_details(request, pk):
    book_image = get_object_or_404(BookImage, pk=pk)
    serializer = BookImageSerializer(book_image)
    return Response(serializer.data, status=status.HTTP_200_OK)

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return AddBookSerializer
        elif self.request.method == 'POST':
            return AddBookSerializer
        return BookSerializer

class BookImageViewSet(viewsets.ModelViewSet):
    queryset = BookImage.objects.all()
    serializer_class = BookImageSerializer

    def perform_create(self, serializer):
        print("KWARGS IN PERFORM_CREATE: ", self.kwargs )
        book_id = self.kwargs.get("book_pk")
        if not book_id:
            raise ValueError("book_id is required")
        serializer.save(book_id=book_id)

@permission_classes([IsAuthenticated])
@api_view(['POST'])
def borrow_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    user = request.user
    data = BookInstanceSerializers(data=request.data)
    data.is_valid(raise_exception=True)
    book_instance = BookInstance()
    book_instance.user = user
    book_instance.book = book
    book_instance.return_date = data.validated_data['return_date']
    book_instance.comments = data.validated_data['comments']
    book_instance.save()
    return Response({'message' : "book borrowed successfully"},status=status.HTTP_200_OK )