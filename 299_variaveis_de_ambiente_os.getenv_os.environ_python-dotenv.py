# Variáveis de ambiente com Python
# Referentes ao seu sistema operacional

# Em um projeto você pode ter:
# Ambiente Local, Ambiente de Testes, Ambiente de Produção

# Para variáveis de ambiente - comandos
# Windows PS: $env:VARIAVEL="Digite a senha" | dir env:
# Linux e Mac: export NOME_VARIAVEL="VALOR" | echo $VARIAVEL

# Para obter o valor das variáveis de ambiente
# No código Python
# os.getenv ou os.environ['VARIAVEL']

# Para configurar variáveis de ambiente
# os.environ['VARIAVEL'] = 'valor'
# Ou usando python-dotenv e o arquivo .env
# pip install python-dotenv - ativar o ambiente virtual
# from dotenv import load_dotenv
# load_dotenv() - arquivo que carrega todas as variáveis de ambiente
# https://pypi.org/project/python-dotenv/
# OBS.: sempre lembre-se de criar um .env-example


import os

#acessa a variável de sistema criada pelo prompt
print(os.getenv('SENHA'))

#assim pode-se utilizar os valores da variável de ambiente
#dentro do programa
senha = os.getenv('SENHA')
print(senha)

# Arquivo .env - example
# indica para outros dev que 
# deve ser criado um arquivo .env nesse modelo
# adaptado às variáveis do sistema operacional que será utilizado
# BD_USER="CHANGE-ME" 
# BD_PASSWORD="jdndb551g#@"
# BD_PORT=3306
# BD_HOST="localhost"

from dotenv import load_dotenv # type: ignore

#precisa criar o arquivo na raiz do projeto - .env
#arquivo não é salvo no git
#possui informações de sistema, usuários e senhas
load_dotenv()

print(os.environ) #dicionário com todas as variáveis de ambiente
print(os.getenv('BD_PASSWORD')) #imprime determinada variavel