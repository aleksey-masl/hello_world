from django.shortcuts import render # этот модуль предназначен для отображения
from django.http import HttpResponse         # готовых HTML - страничек

# Create your views here.

def index(request):
    return HttpResponse("<center><h2> Hello World from Python GJANGO!!!</h2></center>")
