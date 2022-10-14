import requests
from bs4 import BeautifulSoup
from datetime import datetime
from itertools import count

with open(f'noticiasCNN.html', 'w') as arquivo:
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
        arquivo.write(
            '''
    <div>
        <a href="#https://www.cnnbrasil.com.br/politica/">Política</a>
        <a href="#https://www.cnnbrasil.com.br/nacional/">Nacional</a>
        <a href="#https://www.cnnbrasil.com.br/business/">Business</a>
        <a href="#https://www.cnnbrasil.com.br/internacional/">Internacional</a>
        <a href="#https://www.cnnbrasil.com.br/esporte/">Esporte</a>
        <a href="#https://www.cnnbrasil.com.br/saude/">Saude</a>
        <a href="#https://www.cnnbrasil.com.br/tecnologia/">Tecnologia</a>
        <a href="#https://www.cnnbrasil.com.br/entretenimento/">Entretenimento</a>
        <a href="#https://www.cnnbrasil.com.br/estilo/">Estilo</a>
        <a href="#https://www.cnnbrasil.com.br/loterias/">Loterias</a>
    </div>
            '''
        )
        arquivo.write(f'<div class="titulo"><h1 id="{links}">Seção do Site:</h1> <a href="{links}" target="_blanck">'
        f'{links}</a> </div>')
        contador = count(1)
        for noticias in html.select('.home__list__item'):
            tituloMateria = noticias.a.get_text()
            linkMateria = noticias.a.get('href')
            arquivo.write(f'<div class="titulo"> <h2>Nº {next(contador)} | Horario do Scraping: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}'
            f' </h2> '
            f'<h3>{tituloMateria}</h3> <a href="{linkMateria}" target="_blanck">Link Materia</a> ')
            resp = requests.get(linkMateria)
            html1 = BeautifulSoup(resp.text, 'html.parser')
            for materia in html1.select('.posts'):
                dataMateria = materia.select_one('.post__data').get_text(strip=True)
                texto = materia.select_one('.post__content').get_text(' | ', strip=True)
                arquivo.write(f'<h3>Data Matéria: {dataMateria}</h3> </div>')
                arquivo.write(f'<div> <p>{texto}</p> </div>')
    arquivo.write(
        '''
</body>
</html>
        '''
    )
