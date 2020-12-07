from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse("OK")

def info(request):
    return HttpResponse("<html><body><b>INFO PAGE</b><body></html>")