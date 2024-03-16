import pandas as pd
from googletrans import Translator
import os
import time
import matplotlib.pyplot as plt

# Função para traduzir as frases em inglês para o português
def traduzir_frases(texto_ingles):
    translator = Translator()
    traducao = translator.translate(texto_ingles, src='en', dest='pt')
    return traducao.text

# Função para fazer a tradução
def traduzir_conteudo(dados):
    # Aqui vamos traduzir todas as frases na primeira coluna
    dados.iloc[:, 0] = dados.iloc[:, 0].apply(traduzir_frases)
    return dados

# Caminho do arquivo CSV
caminho_arquivo = '/tweets.csv' 

# Verifica se o arquivo existe no caminho especificado
if os.path.exists(caminho_arquivo):
       inicio_execucao = time.time() 
    dados = pd.read_csv(caminho_arquivo)

    # Chamar a função para fazer a tradução
    dados_traduzidos = traduzir_conteudo(dados)

    # Salvar os dados traduzidos em um novo arquivo CSV
    nome_arquivo_traduzido = 'tweets_traduzido.csv'  
    dados_traduzidos.to_csv(nome_arquivo_traduzido, index=False)

    fim_execucao = time.time()  # Registra o tempo de término da execução
    duracao_execucao = fim_execucao - inicio_execucao  # Calcula a duração da execução em segundos

    print("Tradução concluída. O arquivo", nome_arquivo_traduzido, "foi criado com as frases traduzidas.")
    print("Duração da execução:", duracao_execucao, "segundos")

    # Plota o gráfico
    plt.bar(['Execução'], [duracao_execucao])
    plt.ylabel('Tempo de execução (s)')
    plt.title('Performance de Execução')
    plt.show()
else:
    print("O arquivo", caminho_arquivo, "não foi encontrado.")
