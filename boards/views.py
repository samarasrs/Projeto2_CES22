from django.shortcuts import render
from .models import Board
from .scrap import Numeros,Scrap

# Create your views here.
#from django.http import HttpResponse
from django.http import HttpResponse

def home(request):
    return HttpResponse('Hello, World!')

def index(request):
    numerodiario = Scrap()
    return render(request,'index.html',{'numerodiario':numerodiario})