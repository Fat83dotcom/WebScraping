import requests
from bs4 import BeautifulSoup

with open('noticias.txt', '+a') as arquivo:
    url = 'https://www.cnnbrasil.com.br/politica/'
    resposta = requests.get(url)
    html = BeautifulSoup(resposta.text, 'html.parser')

    for links in html.select('.home__list__item'):
        tituloMateria = links.a.get_text()
        linkMateria = links.a.get('href')
        arquivo.write(tituloMateria)
        arquivo.write(linkMateria)
        print(tituloMateria)
        print(linkMateria)
        resp = requests.get(linkMateria)
        html1 = BeautifulSoup(resp.text, 'html.parser')
        for texto in html1.select('.post__content'):
            texto = texto.get_text()
            arquivo.write(texto)
            print(texto, '\n')
