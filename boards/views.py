from django.shortcuts import render
from .scrap import Numeros,Scrap
from django.views.generic import TemplateView
from django.http import HttpResponse
from .models import BrazilData, SudesteData, SaoPauloData


class DataChartView(TemplateView):
    template_name = 'boards/chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"]= BrazilData.objects.all()
        return context

#def home(request):
    #return HttpResponse('Hello, World!')


def index(request):
    numerodiario = Scrap()
    return render(request,'index.html',{'numerodiario':numerodiario})