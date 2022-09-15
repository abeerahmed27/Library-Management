from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import AddBook
from .models import RBook

# Create your views here.
def home(request):
    return HttpResponse("Library Management")

def add(request):
    dest = AddBook.objects.all()
    return render(request,'Templates/Add.html',{'dests' : dest})

def showbooks(request):
    books= RBook.objects
    return render(request,'Templates/Retrieve.html',{'books':books})