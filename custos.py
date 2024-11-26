import xlrd
import pandas as pd
import numpy as np
import mysql.connector
import datetime

conexao = mysql.connector.connect(
    host="192.168.1.110",
    user="dashboard-ti",
    password="rSgX6W72gWMroqyrP1Hs",
    database="dashboard-ti",
    pool_reset_session="False"   # Evita o reset da sessão
)

cursor = conexao.cursor()

'''# Carregar a planilha Excel .xls
caminho_planilha = 'D:/Luan/Downloads/CPD.xls'

# Usar xlrd para abrir o arquivo
workbook = xlrd.open_workbook(caminho_planilha)
sheet = workbook.sheet_by_index(0)  # Assumindo que a planilha está na primeira aba

# Converter os dados para um DataFrame pandas
dados = []
for row in range(sheet.nrows):
    dados.append(sheet.row_values(row))
dados = pd.DataFrame(dados)'''

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
ano_corrente = datetime.datetime.now().year


def criar_dicionario_meses(ano_corrente, meses):
    dicionario_meses = {}
    for i, mes in enumerate(meses, start=1):
        numero_mes = str(i).zfill(2)  # Formatar o número do mês para ter dois dígitos
        data_mes = f"{ano_corrente}-{numero_mes}"
        dicionario_meses[mes] = data_mes
    return dicionario_meses

dicionario_meses = criar_dicionario_meses(ano_corrente, meses)

# Carregar a planilha Excel
caminho_planilha = 'D:/Luan/Downloads/CPD.xlsx'
dados = pd.read_excel(caminho_planilha)
dados.fillna(0, inplace=True) # Substituir valores ausentes por 0

def importar_dados(dados, meses, inicio, fim, dicionario_meses, categoria):
    # Convertendo o DataFrame em uma matriz numpy
    matriz_dados = dados.values

    # Encontrar os índices de cada mês
    for mes in meses:
        # Encontrar o índice da linha que contém as palavras "DESPESAS COM PESSOAL"
        indice_linha_saidas = dados[dados.iloc[:, 0].astype(str).str.contains(f'{inicio}', case=False)].index[0]

        # Encontrar o índice da linha que contém a palavra "DESPESAS ADMINISTRATIVAS"
        indice_linha_despesas = dados[dados.iloc[:, 0].astype(str).str.contains(f'{fim}', case=False)].index[0]

        # Convertendo o DataFrame em uma matriz numpy
        matriz_dados = dados.values

        # Encontrando a linha e a coluna onde está a palavra "Janeiro"
        indice_linha, indice_coluna = np.where(matriz_dados == mes)

        # Convertendo o índice da linha e da coluna para inteiros
        indice_linha = indice_linha[0]  # Supondo que haja apenas uma ocorrência do "Mês"
        indice_coluna = indice_coluna[0]

        # Selecionar os dados entre essas linhas apenas da primeira coluna e da coluna de índice 2 (terceira coluna)
        dados_selecionados = dados.iloc[indice_linha_saidas+1:indice_linha_despesas, [0, indice_coluna]]

        # Converter os dados selecionados para uma lista de listas
        dados_lista = dados_selecionados.values.tolist()

        #Limpa os números na primeira coluna
        for linha in dados_lista:
            # Dividir a linha em duas colunas com base no caractere " - "
            partes = linha[0].split(' - ', 1)
            if len(partes) > 1:
                linha[0] = partes[1].upper()  # Manter apenas a segunda parte
            else:
                linha[0] = partes[0].upper()  # Se não houver " - ", manter toda a linha

        #Tira o sinal de negativo da segunda coluna
        for linha in dados_lista:
            linha[1] = str(linha[1]).replace('-', '')

        setor = 'Tecnologia'
        # Obter a data correspondente ao mês atual
        data_mes_atual = dicionario_meses[mes]

        for linha in dados_lista:
            descricao = linha[0]
            realizado = linha[1]

            # Verificar se a combinação de descricao, setor e data já existe na tabela
            cursor.execute("SELECT * FROM custos WHERE descricao = %s AND setor = %s AND data = %s",
                           (descricao, setor, data_mes_atual))
            resultado = cursor.fetchone()

            if resultado:
                # Se já existir, atualizar a linha existente
                cursor.execute("UPDATE custos SET realizado = %s WHERE descricao = %s AND setor = %s AND data = %s",
                               (realizado, descricao, setor, data_mes_atual))
            else:
                # Se não existir, inserir uma nova linha
                cursor.execute("INSERT INTO custos (descricao, realizado, setor, data, categoria) VALUES (%s, %s, %s, %s, %s)",
                               (descricao, realizado, setor, data_mes_atual, categoria))

        # Commit das alterações
        conexao.commit()

importar_dados (dados, meses, 'DESPESAS COM PESSOAL','DESPESAS ADMINISTRATIVAS', dicionario_meses, 'pessoal')
importar_dados (dados, meses, 'DESPESAS ADMINISTRATIVA','INVESTIMENTOS', dicionario_meses, 'administrativa')
importar_dados (dados, meses, 'INVESTIMENTOS ','FIM', dicionario_meses, 'investimentos')





