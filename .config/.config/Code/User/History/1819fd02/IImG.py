from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from .models import Books

# Create your views here.
def add_Book(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("urf-8"))
        book = Books.objects.create(
            name=data["name"],
            author=data["author"],
            completed=data["completed"]
        )
        return JsonResponse({"id":book.id, "message": "Book created"}, status=201)
    return JsonResponse({"error": "POST required"}, status=400)