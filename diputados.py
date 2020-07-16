#extraer datos web
import urllib
import urllib.request
from bs4 import BeautifulSoup

def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata

url = "https://www.camara.cl/diputados/diputados.aspx#mostrarDiputados"
soup = make_soup(url)

tabla_diputados = soup.find("div", {"id": "ContentPlaceHolder1_ContentPlaceHolder1_pnlDiputadosLista"})

lista = tabla_diputados.find_all('article')
lista[10]
lista[10].find('img')
lista[10].find('img').get('title')
lista[0].find_all('p')[1].text

diputados = []
partidos = []
id_diputado = []
distrito= []

for persona in lista:
    diputados.append(persona.find('img').get('title'))
    partidos.append(persona.find_all('p')[1].text)
    distrito.append(persona.find_all('p')[0].text)
    id_diputado.append(str(persona.find('img').get('src')).split("ID=GRCL")[1])

diputados
partidos

import pandas as pd
df = pd.DataFrame(list(zip(diputados, partidos, id_diputado,distrito)), 
               columns =['senador', 'partido','id_diputado','distrito']) 
df.head()

df.to_csv('diputados.csv')
