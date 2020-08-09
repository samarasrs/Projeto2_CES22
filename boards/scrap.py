
import requests
from bs4 import BeautifulSoup


#file = open("casos.txt","+w")

class Numeros():
    def __init__(self,total,mortes,recuperados):
        self.total = total
        self.mortes = mortes
        self.recuperados = recuperados



def Scrap():

    print("Fazendo request")
    page = requests.get('https://www.worldometers.info/coronavirus/country/brazil/')

    soup = BeautifulSoup(page.text, 'html.parser')

    casos = soup.find_all(class_='maincounter-number')

    
    totalA = casos[0].find('span')
    total = totalA.contents[0]

    mortesA = casos[1].find('span')
    mortes = mortesA.contents[0]

    recuperadosA = casos[2].find('span')
    recuperados = recuperadosA.contents[0]
    print("Dados Ok!\n")

    print("Escrevendo no Txt\n")
    #file.write("Numero de casos total: "+total+"\n")
    #file.write("Numero de mortos total: "+mortes+"\n")
    #file.write("Numero de recuperados total: "+recuperados+"\n")
    print("Sucesso!\n")

    diaria = Numeros(total,mortes,recuperados)
    #file.close()
    return diaria