#caminho = r'C:\\Users\\GabrielCG\\Desktop\\pasta'

# montar um caminho, garantindo compatibilidade entre sistemas operacionais.
caminho = os.path.join('/Users', 'GabrielCG', 'Desktop', 'pasta')

#print(caminho)

#lista todos os arquivos e subpastas dentro de caminho
for pasta in os.listdir(caminho): #pastas dentro da pasta
    caminho_completo_subpasta = os.path.join(caminho, pasta) #caminho + pasta interna
    print(caminho_completo_subpasta)

    if not os.path.isdir(caminho_completo_subpasta): #verifica se o item é uma pasta.
        continue

    for imagem in os.listdir(caminho_completo_subpasta):
        print(imagem) #lista os arquivo dentro da subpasta