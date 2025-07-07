from django.urls import path, include
from rest_framework_nested import routers

from .views import BookViewSet, BookImageViewSet
from . import views

# Base router
router = routers.DefaultRouter()
router.register('books', BookViewSet, basename='books')

router.register('images', BookImageViewSet, basename='images')


book_image_router = routers.NestedDefaultRouter(router, 'books', lookup='book')

book_image_router.register('images', BookImageViewSet, basename='book-images')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(book_image_router.urls)),

    path("book", views.get_books),
    path("greet/<name>", views.greet),
    path("authors/", views.AddAuthorView.as_view(), name='add_author'),
    path("authors/<int:pk>/", views.GetUpdateDestroyAPIView.as_view()),
    path('images/<int:pk>', views.image_details, name='image_details'),
    path ('books/<int:pk>', views.borrow_book, name='borrow_book'),
]