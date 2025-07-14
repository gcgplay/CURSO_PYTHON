# requests para requisições HTTPMore actions
# Tutorial -> https://youtu.be/Qd8JT0bnJGs

# No terminal deixar o servidor do site rodando 
# clear ; venv/bin/python -m http.server -d aula_310_site/ 3333
# verifica no navegador se está funcionando

import requests #fazer requisições ao servidor

# http:// -> 80
# https:// -> 443
url = 'http://localhost:3333/'
response = requests.get(url) #médodo(endereço)

print(response.status_code) #200 success
# print(response.headers) #cabeçalhos
# Inspecionar --> Network --> Headers
# print(response.content) #conteúdo
# print(response.json()) #conteúdo em formado json
print(response.text) #conteúdo em formato texto