# + Web Scraping com Python usando requests e bs4 BeautifulSoupMore actions
# - Web Scraping é o ato de "raspar a web" buscando informações de forma
# automatizada, com determinada linguagem de programação, para uso posterior.
# - O módulo requests consegue carregar dados da Internet para dentro do seu
# código. Já o bs4.BeautifulSoup é responsável por interpretar os dados HTML
# em formato de objetos Python para facilitar a vida do desenvolvedor.
# - Doc: https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/
# + Instalação
# - pip install requests types-requests bs4
import re

import requests
from bs4 import BeautifulSoup

url = 'http://127.0.0.1:3333/'
response = requests.get(url) #puxa o conteúdo da url
raw_html = response.text #recebe o conteúdo da url em formato txt
parsed_html = BeautifulSoup(raw_html, 'html.parser')

# retorna mais de uma coisa - exige checagem (if)
# if parsed_html.title is not None:
#     print(parsed_html.title.text)

top_jobs_heading = parsed_html.select_one('#intro > div > div > article > h2') #para localizar/selecionar uma tag

#precisa checar, pois pode retornar mais de um coisa
if top_jobs_heading is not None:
    article = top_jobs_heading.parent

    if article is not None:
        for p in article.select('p'):
            print(re.sub(r'\s{1,}', ' ', p.text).strip()) #imprime tudo dentro dos paragráfos do article, corrigindo os espaços com expressão regular (re)

# Caso queira mudar a codificação de caracteres, envie os bytes diretamente para o BeautifulSoup e passe o valor da codificação de caracteres no atributo "from_encoding". Exemplo (para utf-8):

# BeautifulSoup(response.content, 'html.parser', from_encoding='utf-8')
# Perceba que troquei "response.text" para "response.content" para obter os bytes ao invés da string.