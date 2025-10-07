from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from .models import Books
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def add_Book(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        book = Books.objects.create(
            name=data["name"],
            author=data["author"],
            completed=data["completed"]
        )
        return JsonResponse({"id":book.id, "message": "Book created"}, status=201)
    return JsonResponse({"error": "POST required"}, status=400)

@csrf_exempt
def show_Book(request):
    if request.method == "GET":
        books = Books.objects.all().values
        return JsonResponse(list(books), status=200)


@csrf_exempt
def remove_Book(request):
    pass