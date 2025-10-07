from django.urls import path
from . import views

urlpatterns = [
    path("books/create/", views.add_Book, name="add-book"),
    path("books/", views.show_Book, name="show-book"),
    path("books/delete", views.remove_Book, name="remove-book"),
]