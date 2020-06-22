from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def quote(request):
    return render(request, "quote/form.html")


def history(request):
    return render(request, "quote/history.html")

def registerClient(request):
    return render(request,"quote/registerClient.html")

def login(request):
    return render(request, "quote/login.html")

def profileManager(request):
    return render(request, "quote/profileManager.html")

def home(request):
    return render(request, "quote/home.html")
