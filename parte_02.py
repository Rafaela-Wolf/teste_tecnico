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
    with open('custo_pt_02.csv', 'r') as leitor_csv:
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
    return None
    
cidade_origem = encontrar_cidades_correspondentes(cep_origem, dados_da_cidade)
cidade_destino = encontrar_cidades_correspondentes(cep_destino, dados_da_cidade)

def encontrar_rota_mais_barata(cidade_origem, cidade_destino, dados_de_custo):
    cidades_visitadas = set()
    cidades_nao_visitadas = set()
    menor_distancia = {}
    cidade_anterior = {}

    for (cidade1, cidade2) in dados_de_custo:
        cidades_nao_visitadas.add(cidade1)
        cidades_nao_visitadas.add(cidade2)
    
    for cidade in cidades_nao_visitadas:
        cidade_anterior[cidade] = None
        menor_distancia[cidade] = float('inf')
    menor_distancia[cidade_origem] = 0

    while cidades_nao_visitadas:
        cidade_atual = None
        menor_distancia_atual = float('inf')
        for cidade in cidades_nao_visitadas:
            if menor_distancia[cidade] < menor_distancia_atual:
                menor_distancia_atual = menor_distancia[cidade]
                cidade_atual = cidade

        if cidade_atual == None:
             break
        
        cidades_visitadas.add(cidade_atual)
        cidades_nao_visitadas.remove(cidade_atual)

        for (vizinho1, vizinho2), custo in dados_de_custo.items():
            vizinho = None
            if vizinho1 == cidade_atual and vizinho2 in cidades_nao_visitadas:
                vizinho = vizinho2
            elif vizinho2 == cidade_atual and vizinho1 in cidades_nao_visitadas:
                vizinho = vizinho1

            if vizinho:
                distancia_atual = menor_distancia[cidade_atual] + custo
                if distancia_atual < menor_distancia[vizinho]:
                    menor_distancia[vizinho] = distancia_atual
                    cidade_anterior[vizinho] = cidade_atual

        if cidade_atual == cidade_destino:
            break

    rota = []
    cidade = cidade_destino
    while cidade != None:
        rota.insert(0, cidade)
        cidade = cidade_anterior[cidade]

    custo_total = menor_distancia.get(cidade_destino, float('inf'))
    return rota, custo_total

if cidade_origem and cidade_destino:
    print(f"O CEP de origem {cep_origem} pertence à cidade {cidade_origem}.")
    print(f"O CEP destino {cep_destino} pertence à cidade {cidade_destino}.")
    rota, custo = encontrar_rota_mais_barata(cidade_origem, cidade_destino, dados_de_custo)
    if custo == float('inf'):
        print(f"Não há rotas entre a cidade {cidade_origem} e a cidade {cidade_destino}.")
    else:
        print(f"A rota mais barata da cidad {cidade_origem} para a cidade {cidade_destino} é: {rota}")
        print(f"O custo total da rota é: R${custo:.2f}")
else:
    print("Não existe cidade correspondente para um ou ambos os CEPs.")