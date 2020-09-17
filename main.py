from datetime import datetime
import os
opcao = None
sabor = []
valor = []
tamanho = []
data = []
item_compra = []
valor_compra = []
data_compra = []


quantidade = 0


def venda(sabor, valor, data, tamanho):
    cadastro_nome = input("digite o nome sabor: ")
    cadastro_tamanho = input('Digite o tamanho B, M, G ou F: ')
    cadastro_preco = input("digite o valor: ")
    if cadastro_preco.isdigit():
        sabor.append(cadastro_nome)
        tamanho.append(cadastro_tamanho)
        valor.append(float(cadastro_preco))
        data.append(datetime.today())
    else:
        cadastro_preco = input("valor incorreto, digite novamente: ")
        sabor.append(cadastro_nome)
        valor.append(float(cadastro_preco))
        data.append(datetime.today())


def mostrar_venda():
    for mostrar_sabor, mostrar_valor, mostrar_data, mostrar_tamanho in zip(sabor, valor, data, tamanho):
        print(f'Sabor:{mostrar_sabor}')
        print(f'Tamanho:{mostrar_tamanho}')
        print(f'Valor:{mostrar_valor}')
        print(f'Data:{mostrar_data} ')
        print('--------------------------\n')

def gerar_relatorio(valor):
    total_venda = 0
    for valor_venda in valor:
        total_venda += float(valor_venda)

    return total_venda



while (opcao != 0):
    
    print("-----cadastro de venda e relatórios-------\n")
    print("1 - para cadastrar uma venda\n")
    print("2 - para cadastrar uma compra\n")
    print("3 - mostrar as vendas\n")
    print("4 - mostrar as compras\n")
    print("6 - mostrar total: lucro, compras e vendas\n")
    print("0 - para sair\n")
    print(" \n")
    opcao = int(input("Digite uma opção: "))
    os.system("cls")
    if opcao == 1:
        venda(sabor, valor, data, tamanho)

    elif opcao == 2:
        print('ainda não implementado') 

    elif opcao == 3:
        mostrar_venda()
        
    elif opcao == 4:
        print('ainda não implementado')

    elif opcao == 5:
        print('ainda não implementado')

    elif opcao == 6:
        print(f'Valor total de venda: {float(gerar_relatorio(valor))} \n')
                

    elif opcao == 0:
        print('Programa encerrado')


    else:
        print("opção inválida")

print("---- Fim do programa---\n")
