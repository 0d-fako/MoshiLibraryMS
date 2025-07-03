from django.urls import path, include
from rest_framework_nested.routers import DefaultRouter, NestedDefaultRouter

from .views import BookViewSet, BookImageViewSet
from . import views

# Base router
router = DefaultRouter()
router.register(r'books', BookViewSet, basename='books')

# Nested router: book → images
books_router = NestedDefaultRouter(router, r'books', lookup='book')
books_router.register(r'images', BookImageViewSet, basename='book-images')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(books_router.urls)),

    path("book", views.get_books),
    path("greet/<name>", views.greet),
    path("author/", views.AddAuthorView.as_view(), name='add_author'),
    path("authoer/<int:pk>/", views.GetUpdateDestroyAPIView.as_view()),
    path('images/<int:pk>', views.image_details, name='image_details'),
]