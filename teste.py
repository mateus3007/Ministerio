import requests
import csv
import matplotlib.pyplot as plt
import zipfile
import os

# Função para fazer o download do arquivo .zip
def baixar_arquivo_zip(https://repositorio.dados.gov.br/seges/detru/, sincov_consorcios.csv.zip):
    resposta = requests.get(url)
    with open(nome_arquivo_zip, 'wb') as arquivo_zip:
        arquivo_zip.write(resposta.content)

# Função para descompactar o arquivo .zip
def descompactar_arquivo_zip(nome_arquivo_zip, pasta_destino):
    with zipfile.ZipFile(nome_arquivo_zip, 'r') as zip_ref:
        zip_ref.extractall(pasta_destino)

# Função para acessar o link direto
def acessar_link():
    url = 'siconv_consorcios.csv.zip'
    resposta = requests.get(url)
    if resposta.status_code == 200:
        conteudo = resposta.text
        print(conteudo)
        # Faça algo com o conteúdo retornado, se necessário
    else:
        print('Falha ao acessar o link direto:', resposta.status_code)

# Função para ler e filtrar os dados do arquivo CSV e criar o gráfico
def ler_csv_filtrar_dados_criar_grafico():
    arquivo_csv = 'seu_arquivo.csv'  # Substitua pelo caminho do seu arquivo CSV
    coluna_filtro = 1  # Índice da coluna a ser filtrada (começando em 0)

    x_valores = []
    y_valores = []

    with open(arquivo_csv, 'r') as file:
        leitor_csv = csv.reader(file)

        for linha in leitor_csv:
            if len(linha) > coluna_filtro:
                valor_coluna = float(linha[coluna_filtro])
                # Aplicar a lógica de filtro desejada
                if valor_coluna >= 10 and valor_coluna <= 50:
                    x_valores.append(float(linha[0]))
                    y_valores.append(valor_coluna)

    plt.plot(x_valores, y_valores)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Gráfico de Linhas')
    plt.savefig('grafico.png')
    plt.show()

# URL do arquivo .zip que você deseja baixar
url_arquivo_zip = 'https://www.example.com/arquivo.zip'
nome_arquivo_zip = 'arquivo.zip'

# Pasta de destino para a descompactação do arquivo .zip
pasta_destino = 'pasta_destino'

# Baixar o arquivo .zip
baixar_arquivo_zip(url_arquivo_zip, nome_arquivo_zip)

# Descompactar o arquivo .zip
descompactar_arquivo_zip(nome_arquivo_zip, pasta_destino)

# Acessar o link direto
acessar_link()

# Ler o arquivo .csv, filtrar os dados e criar o gráfico
ler_csv_filtrar_dados_criar_grafico()

# Remover o arquivo .zip e a pasta de destino (opcional)
os.remove(nome_arquivo_zip)
os.rmdir(pasta_destino)
