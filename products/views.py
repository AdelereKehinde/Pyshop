import django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('Hello World')

# Create your views here.
