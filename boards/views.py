from django.shortcuts import render
from .models import Board
from .scrap import Numeros,Scrap, getgraphicbrasil, getgraphicSP


# Create your views here.
#from django.http import HttpResponse

def home(request):
    boards = Board.objects.all()
    return render(request,'home.html',{'boards':boards})

def index(request):
    numerodiario = Scrap()
    graficobrasil = getgraphicbrasil()
    graficoSP = getgraphicSP()
    return render(request,'index.html',{'numerodiario':numerodiario, 'graficobrasil':graficobrasil, 'graficoSP':graficoSP})

