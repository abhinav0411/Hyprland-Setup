from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.

def function(request):
    return HttpResponse("Hello world")

class HelloXYZ(View):
    def get(self, request):
        return HttpResponse("Hello XYZ")
    
    
