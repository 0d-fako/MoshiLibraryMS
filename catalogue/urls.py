from django.urls import path


from . import views

urlpatterns = [
    path("catalogue/book", views.get_books),
]