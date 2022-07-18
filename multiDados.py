import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_noticias = []

#response recebe a resposta do site
response = requests.get('https://g1.globo.com/')

#content recebe o conteudo da requisição
content = response.content

#convertemos o resultado para o tipo html, para mais visibilidade e organização
site = BeautifulSoup(content, 'html.parser')

#vamos encontrar todas as noticias, ou melhor todas que tenham a div class 'feed-post-body'
noticias = site.findAll('div', attrs={'class': 'feed-post-body'})

for noticia in noticias:

    titulo = noticia.find('a', attrs={'class': 'feed-post-link'})
    resumo = noticia.find('div', attrs={'class': 'feed-post-body-resumo'})
    #print(titulo.text)
    #print(titulo['href'])#acessando de foma dicionario para pegar o link da matéria

    if (resumo):
        lista_noticias.append([titulo.text, resumo.text, titulo['href']])
    else:
        lista_noticias.append([titulo.text, '', titulo['href']])  

news = pd.DataFrame(lista_noticias, columns=['Título', 'Subititulo', 'Link'])

news.to_csv('dados.csv', index=False)
print(news)
