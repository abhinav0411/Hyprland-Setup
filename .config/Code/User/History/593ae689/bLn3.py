from django.urls import path
from . import views

urlpatters = [
    path('fuction', views.function),
    path('class', views.HelloXYZ.as_view())
]