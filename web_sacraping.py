import requests
from bs4 import BeautifulSoup
from datetime import datetime
from itertools import count

with open('noticias.txt', 'a+') as arquivo:
    url = 'https://www.cnnbrasil.com.br/politica/'
    resposta = requests.get(url)
    html = BeautifulSoup(resposta.text, 'html.parser')
    contador = count(1)
    for links in html.select('.home__list__item'):
        tituloMateria = links.a.get_text()
        linkMateria = links.a.get('href')
        arquivo.write(f'{next(contador)} Horario do Scraping: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}\n{tituloMateria}\n{linkMateria}')
        print(tituloMateria)
        print(linkMateria)
        resp = requests.get(linkMateria)
        html1 = BeautifulSoup(resp.text, 'html.parser')
        for texto in html1.select('.post__content'):
            texto = texto.get_text()
            arquivo.write(f'\n{texto}\n')
            print(texto, '\n')
