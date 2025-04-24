import csv

def ler_primeiro_arquivo():
    with open('dados_pt_02.csv', 'r') as arquivo_csv:
            dados_da_cidade = {}
            conteudo = csv.DictReader(arquivo_csv)
            for linha in conteudo:
                cidade = linha['Cidade']
                cep_inicial = int(linha['CepInicial'])
                cep_final = int(linha['CepFinal'])
                dados_da_cidade[cidade] = [cep_inicial, cep_final]
            return dados_da_cidade

def ler_segundo_arquivo():
    with open('custo_parte_02.csv', 'r') as leitor_csv:
        dados_de_custo = {}
        leitor = csv.DictReader(leitor_csv)
        for linha in leitor:
                cidade1 = linha['Cidade1']
                cidade2 = linha['Cidade2']
                custo_transporte = float(linha['CustoTransporte'])
                dados_de_custo[(cidade1, cidade2)] = custo_transporte      
        return dados_de_custo

dados_da_cidade = ler_primeiro_arquivo()
dados_de_custo = ler_segundo_arquivo()

cep_origem = 10001086
cep_destino = 80000245

def encontrar_cidades_correspondentes(cep, dados_da_cidade):
    for cidade, intervalo_ceps in dados_da_cidade.items():
         cep_inicial, cep_final = intervalo_ceps
         if cep_inicial <= cep <= cep_final:
              return cidade
    return print("CEP não encontrado em nenhuma cidade.")
    
cidade_origem = encontrar_cidades_correspondentes(cep_origem, dados_da_cidade)
cidade_destino = encontrar_cidades_correspondentes(cep_destino, dados_da_cidade)

if cidade_origem and cidade_destino:
    print(f"O CEP de origem {cep_origem} pertence à cidade {cidade_origem}.")
    print(f"O CEP destino {cep_destino} pertence à cidade {cidade_destino}.")

def encontrar_rota_mais_barata():
     cidades_visitadas = []
     menor_distancia = {}
     cidade_anterior = {}
