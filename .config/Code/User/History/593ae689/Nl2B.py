from django.urls import path
from . import views

urlpatterns = [
    path('function', views.function),
    path('class', views.HelloXYZ.as_view())
]