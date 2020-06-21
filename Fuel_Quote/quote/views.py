from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def quote(request):
    return render(request, "quote/form.html")


def history(request):
    return render(request, "quote/history.html")