import requests
from bs4 import BeautifulSoup
from datetime import datetime
from itertools import count

with open(f'noticiasCNN{datetime.now().strftime("%d-%m-%Y-%H-%M-%S")}.html', 'a+') as arquivo:
    url = [
        'https://www.cnnbrasil.com.br/politica/',
        'https://www.cnnbrasil.com.br/nacional/',
        'https://www.cnnbrasil.com.br/business/',
        'https://www.cnnbrasil.com.br/internacional/',
        'https://www.cnnbrasil.com.br/esporte/',
        'https://www.cnnbrasil.com.br/saude/',
        'https://www.cnnbrasil.com.br/tecnologia/',
        'https://www.cnnbrasil.com.br/entretenimento/',
        'https://www.cnnbrasil.com.br/estilo/',
        'https://www.cnnbrasil.com.br/loterias/',
    ]
    arquivo.write(
        '''
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Web Scraping BrainStorm</title>
    <link rel="stylesheet" href="style.css"> 
</head>
<body>
    '''
    )
    for links in url:
        resposta = requests.get(links)
        html = BeautifulSoup(resposta.text, 'html.parser')
        arquivo.write(f'<h1>Seção do Site:</h1> <a href="{links}" target="_blanck">{links}</a> ')
        contador = count(1)
        for noticias in html.select('.home__list__item'):
            tituloMateria = noticias.a.get_text()
            linkMateria = noticias.a.get('href')
            arquivo.write(f'<h2>{next(contador)} Horario do Scraping: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}</h2> '
            f'<h3>{tituloMateria}</h3> <a href="{linkMateria}" target="_blanck">Link Materia</a> ')
            print(tituloMateria)
            print(linkMateria)
            resp = requests.get(linkMateria)
            html1 = BeautifulSoup(resp.text, 'html.parser')
            for texto in html1.select('.post__content'):
                texto = texto.get_text(" | ", strip=True)
                arquivo.write(f'<div> <p>{texto}</p> </div>')
                print(texto, '\n')
    arquivo.write(
        '''
</body>
</html>
        '''
    )
