from django.urls import path


from . import views

urlpatterns = [
    path("catalog/book", views.get_books),
]