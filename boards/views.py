from django.shortcuts import render
from .scrap import Numeros,Scrap
from django.views.generic import TemplateView
from django.http import HttpResponse
from .models import BrazilData, SudesteData, SaoPauloData

'''
class DataChartView(TemplateView):
    template_name = 'boards/chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"]= BrazilData.objects.all()
        return context
'''



def home(request):
    numerodiario = Scrap()
    dates_brazil, cases_brazil, deaths_brazil = getBrazilData()
    context = {'numerodiario': numerodiario, 'dates_brazil': dates_brazil, 'cases_brazil': cases_brazil,'deaths_brazil': deaths_brazil,
               }
    return render(request, 'home.html', context)


def index(request):
    numerodiario = Scrap()


    dados = getBrazilData()
    dados_sudeste = getSudesteData()
    dados_sp = getSaoPauloData()
    context = {'numerodiario':numerodiario, 'dados':dados,'dados_sudeste':dados_sudeste, 'dados_sp':dados_sp
             }
    return render(request, 'index.html', context)


class Dados():
    def __init__(self, dates_brazil, cases_brazil, deaths_brazil):
        self.dates_brazil=dates_brazil
        self.cases_brazil=cases_brazil
        self.deaths_brazil=deaths_brazil


def getBrazilData():
    brazil_list = BrazilData.objects.all()
    cases_brazil = []
    deaths_brazil = []
    dates_brazil = []
    for item in brazil_list:
        cases_brazil.append(item.cases)
        deaths_brazil.append(item.deaths)
        aux = item.date.strftime("%b %d %Y")
        dates_brazil.append(aux)
    print( dates_brazil)
    dados = Dados(dates_brazil, cases_brazil, deaths_brazil)
    return dados

class Dados2():
    def __init__(self, dates_sudeste, cases_sudeste, deaths_sudeste):
        self.dates_sudeste=dates_sudeste
        self.cases_sudeste=cases_sudeste
        self.deaths_sudeste=deaths_sudeste


def getSudesteData():
    sudeste_list = SudesteData.objects.all()
    cases_sudeste = []
    deaths_sudeste = []
    dates_sudeste = []
    for item in sudeste_list:
        cases_sudeste.append(item.cases)
        deaths_sudeste.append(item.deaths)
        aux = item.date.strftime("%b %d %Y")
        dates_sudeste.append(aux)
    print( dates_sudeste)
    dados = Dados2(dates_sudeste, cases_sudeste, deaths_sudeste)
    return dados

class Dados3():
    def __init__(self, dates_sp, cases_sp, deaths_sp):
        self.dates_sp=dates_sp
        self.cases_sp=cases_sp
        self.deaths_sp=deaths_sp


def getSaoPauloData():
    sudeste_list = SaoPauloData.objects.all()
    cases_sp = []
    deaths_sp = []
    dates_sp = []
    for item in sudeste_list:
        cases_sp.append(item.cases)
        deaths_sp.append(item.deaths)
        aux = item.date.strftime("%b %d %Y")
        dates_sp.append(aux)
    print( dates_sp)
    dados = Dados3(dates_sp, cases_sp, deaths_sp)
    return dados

