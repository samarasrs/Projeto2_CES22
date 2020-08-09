from django.shortcuts import render
from .scrap import Numeros,Scrap
from django.views.generic import TemplateView
from django.http import HttpResponse
from .models import BrazilData, SudesteData, SaoPauloData, EstadosData, RegiaoData

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
    dados_regiao= getRegiaoData()
    dados_estados= getEstadosData()
    context = {'numerodiario':numerodiario, 'dados':dados,'dados_sudeste':dados_sudeste, 'dados_sp':dados_sp, 'dados_regiao':dados_regiao, 'dados_estados':dados_estados
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
    dados = Dados3(dates_sp, cases_sp, deaths_sp)
    return dados


class Dados4():
    def __init__(self, cases_estados, deaths_estados):
        self.cases_estados=cases_estados
        self.deaths_estados=deaths_estados


def getEstadosData():
    estados_list = EstadosData.objects.all()
    cases_estados = []
    deaths_estados = []
    for item in estados_list:
        aux1=[]
        aux2=[]
        aux1.append(item.name)
        aux1.append(item.cases)
        aux2.append(item.name)
        aux2.append(item.deaths)
        cases_estados.append(aux1)
        deaths_estados.append(aux2)
    dados = Dados4(cases_estados, deaths_estados)
    return dados

class Dados5():
    def __init__(self, names_regiao, cases_regiao, deaths_regiao):
        self.names_regiao=names_regiao
        self.cases_regiao=cases_regiao
        self.deaths_regiao=deaths_regiao


def getRegiaoData():
    regiao_list = RegiaoData.objects.all()
    cases_regiao = []
    deaths_regiao = []
    names_regiao = []
    for item in regiao_list:
        cases_regiao.append(item.cases)
        deaths_regiao.append(item.deaths)
        names_regiao.append(item.name)
    dados = Dados5(names_regiao, cases_regiao, deaths_regiao)
    return dados