from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Nani')

def page_one(request):
    return HttpResponse('Топор весит килограмм и пол топора, сколько весит топор в килограммах?')