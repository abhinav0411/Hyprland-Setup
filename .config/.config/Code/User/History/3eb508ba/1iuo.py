from django.urls import path
from . import views

urlpatterns = [
    path("/books/create", views.add_Book, name="add-book"),
]