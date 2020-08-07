from django.shortcuts import render
from .models import Board
from .scrap import Numeros,Scrap

# Create your views here.
#from django.http import HttpResponse

def home(request):
    boards = Board.objects.all()
    return render(request,'home.html',{'boards':boards})

def index(request):
    numerodiario = Scrap()
    return render(request,'index.html',{'numerodiario':numerodiario})