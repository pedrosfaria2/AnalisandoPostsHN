import datetime as dt
from collections import defaultdict
import matplotlib.pyplot as plt

# Cria uma tabela de frequência usando a data formatada para nossos dados
def tabela_frequencia_hora(data, coluna = ''): 
    dicionario = defaultdict(int)
    date_format = "%Y-%m-%d %H:%M:%S"
    
    if coluna == '':
        for row in data:
            date_str = row[4]
            date = dt.datetime.strptime(date_str, date_format)
            hora = date.strftime("%H")
            dicionario[(hora)] += 1
    else:
        for row in data:
            date_str = row[4]        
            date = dt.datetime.strptime(date_str, date_format)
            hora = date.strftime("%H")
            dicionario[(hora)] += float(row[coluna])

    dicionario = sorted(dicionario.items(), key=lambda x: int(x[0]))
    
    return dict(dicionario)

# Calcula a média de uma coluna de uma lista
def calcula_media(lista, coluna):
    soma = 0
    for row in lista:
        soma += float(row[coluna])        
    return round(soma / len(lista), 2)

##Gera gráfico de barras de um dicionário
def grafico_barra_dicionario(dicionario, x_label, y_label, title, media_geral=''):

    plt.figure(figsize=(10, 6))
    plt.bar(dicionario.keys(), dicionario.values(), color='skyblue')
    if media_geral != '':
        plt.axhline(y=media_geral, color='red', linestyle='--')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.grid(True)

    plt.show()

# Imprime tabela de um dicionário
def tabela_dicionario(dicionario, label_1, label_2):
    print(f"{label_1}\t{label_2}")
    for chave, valor in dicionario.items():
        print(f"{chave}\t{valor}")
