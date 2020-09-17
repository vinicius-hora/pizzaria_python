produto = []
quantidade = 0
def venda(produto, quantidade):
    nome = input("digite o nome sabor: ")
    valor = input("digite o valor: ")
    dataVenda =
    if valor.isdigit():
        produto = [nome, valor]
    else:
        valor = input("valor incorreto, digite novamente: ")
        produto = [nome, valor]

    print(produto)

venda(produto, quantidade)
print(produto[0:2])