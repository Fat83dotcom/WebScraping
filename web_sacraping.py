import requests
from bs4 import BeautifulSoup

url = 'https://www.cnnbrasil.com.br/politica/'
resposta = requests.get(url)
html = BeautifulSoup(resposta.text, 'html.parser')

for links in html.select('.home__list__item'):
    tituloMateria = links.a.get_text()
    linkMateria = links.a.get('href')
    print(tituloMateria)
    print(linkMateria)
    resp = requests.get(linkMateria)
    html1 = BeautifulSoup(resp.text, 'html.parser')
    for texto in html1.select('.post__content'):
        texto = texto.p.get_text()
        print(texto, '\n')

