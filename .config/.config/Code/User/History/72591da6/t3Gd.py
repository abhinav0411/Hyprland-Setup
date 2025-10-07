from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
todo_dict = {
    1: "something",
    2: "testing"
}

def home(request):
    return render(request, "home.html")

def rooms(request):
    return render(request, "room.html")

