import requests
from bs4 import BeautifulSoup

url_base = 'https://lista.mercadolivre.com.br/'
busca = str(input('o que você quer pesquisar: '))

response = requests.get(url_base + busca)

site = BeautifulSoup(response.text, 'html.parser')

produto = site.find('div', attrs={'class': 'andes-card andes-card--flat andes-card--default ui-search-result ui-search-result--core andes-card--padding-default'})

titulo = produto.find('h2', attrs={'class': 'ui-search-item__title'})

print(produto.prettify())
print(f'Titulo do produto é {titulo.text}')