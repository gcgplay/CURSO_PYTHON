# quando você instalar uma dependência que depende de outra
# para funcionar, o vscode já instala junto as outras dependencias

# pedi automaticamente para INSTALAR o pip
# senão python.exe -m pip istall
# verificar se está no ambiente virtual ativo
# pois se instalar no global irá colocar as versões
# dos pacotes em todos os projetos

# Exemplo - Instalar o pymysql
# pip instal pymysql

# mostrar todas as versões de um pacote
# pip index versions pymysql

# Desinstalar - pip uninstall ptmysql

# Tem que esperar a reativação do ambiente virtual para
# funcionar as alterações

# Ver os pacotes instalados
# pip freeze
# Gera o requeriments.txt que recria novamente o ambiente virtual
# pip freeze > requeriments.txt

# Pode apagar a pasta venv e utilizar requeriments.txt para restaurar
# Pois salva as versões que foram utilizadas naquele projeto
# Gerar uma nova venv
# E executar o comando:
# pip install -r .\requeriments.txt
# Instala todos os pacotes