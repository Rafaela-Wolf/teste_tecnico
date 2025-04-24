import csv

def verificar_cep():
    try:
        with open('dados_pt_01.csv', 'r') as arquivo_csv:
            entrada = int(input("Digite o CEP que você deseja consultar: "))
            conteudo = csv.DictReader(arquivo_csv)
            for linha in conteudo:
                cidade = linha['Cidade']
                cep_inicial = int(linha['CEPInicial'])
                cep_final = int(linha['CEPFinal'])
            
                if entrada <= 0:
                    print("Digite um CEP válido.")  
                    break
                elif cep_inicial <= entrada <= cep_final:
                    print(f"O CEP {entrada} pertence à cidade {cidade}.")
                    break
                else:
                    print(f"O CEP {entrada} não foi encontrado.")
                    break
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except ValueError:
        print("Digite um CEP válido (apenas números).")
    finally:
        print("Operação finalizada.")

verificar_cep()