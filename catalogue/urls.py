from django.urls import path, include
from rest_framework import routers

from .views import BookViewSet, BookImageViewSet

router = routers.DefaultRouter()

router.register('books', BookViewSet, basename='books' )


router.register('images', BookImageViewSet, basename='book-images')


from . import views

urlpatterns = [

    path('', include(router.urls)),
    path("book", views.get_books),
    path("greet/<name>", views.greet),

    path("author/", views.AddAuthorView.as_view(), name='add_author'),

    path("authoer/<int:pk>/", views.GetUpdateDestroyAPIView.as_view()),

    path('images/<int:pk>', views.image_details, name='image_details'),

]