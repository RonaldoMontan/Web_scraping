import requests
from bs4 import BeautifulSoup

#response recebe a resposta do site
response = requests.get('https://g1.globo.com/')

#content recebe o conteudo da requisição
content = response.content

#convertemos o resultado para o tipo html, para mais visibilidade e organização
site = BeautifulSoup(content, 'html.parser')

#dentro do site vamos procurar pela tag div cuja a classe é 'feed-post-body'
#lembrando que podemos procurar outra tag alem da <div>
noticia = site.find('div', attrs={'class': 'feed-post-body'})

#vamos afundar mais um  pouco para encontrar o titulo, que vai seguir a mesma ideia do passo anterior
#dentro d enoticia vamos procurar pela tag a cuja clase é 'feed-post-link' que armazenaremos em titulo
titulo = noticia.find('div', attrs={'class': 'feed-post-body-title'})

resumo = noticia.find('div', attrs={'class': 'feed-post-body-resumo'})


print(titulo.text)
print(resumo.text)
