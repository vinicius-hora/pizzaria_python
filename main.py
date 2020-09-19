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
    while cadastro_preco.isalpha():
        cadastro_preco = input("valor incorreto, digite novamente: ")
        os.system("cls")

    sabor.append(cadastro_nome)
    tamanho.append(cadastro_tamanho)
    valor.append(float(cadastro_preco))
    data.append(datetime.today())
    print("Venda cadastrada \n")
    

def cadastrar_compra(item_compra, valor_compra, data_compra):
    cadastro_item = input("Digite o nome do item comprado ou número da nota: ")
    cadastro_valor = input("Digite o valor da compra: ")
    while cadastro_valor.isalpha():
        cadastro_valor = input("Valor só pode ser númerico, digite novamente: ")
        os.system("cls")
   
    item_compra.append(cadastro_item)
    valor_compra.append(float(cadastro_valor))
    data_compra.append(datetime.today())
    print("Compra cadastrada \n")



def mostrar_venda():
    for mostrar_sabor, mostrar_valor, mostrar_data, mostrar_tamanho in zip(sabor, valor, data, tamanho):
        print(f'Sabor:{mostrar_sabor}')
        print(f'Tamanho:{mostrar_tamanho}')
        print(f'Valor:{mostrar_valor}')
        print(f'Data:{mostrar_data} ')
        print('--------------------------\n')

def mostrar_comra():
    for mostrar_item, mostrar_valor, mostrar_data in zip(item_compra, valor_compra, data_compra):
        print(f'Item: { mostrar_item}')
        print(f'Item: { mostrar_valor}')
        print(f'Item: { mostrar_data}')
        print('--------------------------\n')

def gerar_relatorio_venda(valor):
    total_venda = 0
    for valor_venda in valor:
        total_venda += float(valor_venda)

    return total_venda

def gerar_relatorio_compra(valor_compra):
    total_compra = 0
    for v_compra in valor_compra:
        total_compra+= float(v_compra)

    return total_compra



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
        cadastrar_compra(item_compra, valor_compra, data_compra)

    elif opcao == 3:
        os.system("cls")
        mostrar_venda()
        
    elif opcao == 4:
       os.system("cls")
       mostrar_comra()

    elif opcao == 5:
        print('ainda não implementado')

    elif opcao == 6:
        print(f'Valor total de venda: {float(gerar_relatorio_venda(valor))} \n')
        print(f'Valor total de compra: {float(gerar_relatorio_compra(valor_compra))} \n')
        print(f'Saldo: {float(gerar_relatorio_venda(valor) - gerar_relatorio_compra(valor_compra))} \n')
                

    elif opcao == 0:
        print('Programa encerrado')


    else:
        print("opção inválida")

print("---- Fim do programa---\n")
