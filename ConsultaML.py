import requests
from bs4 import BeautifulSoup

url_base = 'https://lista.mercadolivre.com.br/'
busca = str(input('o que você quer pesquisar: '))

response = requests.get(url_base + busca)

site = BeautifulSoup(response.text, 'html.parser')

produtos = site.findAll('div', attrs={'class': 'andes-card andes-card--flat andes-card--default ui-search-result ui-search-result--core andes-card--padding-default'})

for produto in produtos:

    titulo = produto.find('h2', attrs={'class': 'ui-search-item__title'})

    link = produto.find('a', attrs={'class': 'ui-search-link'})

    moeda = produto.find('span', attrs={'class': 'price-tag-symbol'})
    real = produto.find('span', attrs={'class': 'price-tag-fraction'})
    centavos = produto.find('span', attrs={'class': 'price-tag-cents'})
    valor = str(moeda.text + real.text + ',' + centavos.text)

    #print(produto.prettify())
    print()
    print(url_base + busca)
    print(f'Titulo do produto é {titulo.text}')

    if (centavos):
        print(f'o Valor do produto é {valor}')
    else:
        print('O valor do produto é ', moeda.text + real.text)    
    print('O link do produto é ', link['href'])
    print('\n----------------------------------------\n')