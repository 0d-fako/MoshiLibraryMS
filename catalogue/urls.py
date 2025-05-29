from django.urls import path


from . import views

urlpatterns = [
    path("book", views.get_books),
    path("greet/<name>", views.greet),

]