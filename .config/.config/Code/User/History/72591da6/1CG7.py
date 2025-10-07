from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
todo_dict = {
    1: "something",
    2: "testing"
}

def todo(request):
    return HttpResponse(todo_dict)

def hello(request):
    return HttpResponse("hello world")