
def cadastrar_venda():
    cadastro_sabor = tela_venda.venda_sabor_text.text()
    cadastro_tamanho = tela_venda.venda_tamanho_text.text()
    cadastro_valor = tela_venda.valor_text.text()

    #campos em branco
    tela_venda.venda_sabor_text.setText("")
    tela_venda.venda_tamanho_text.setText("")
    #tela_venda.valor_text.setDouble("0,00")



    #impressao dos dados
    print(cadastro_sabor)
    print(cadastro_tamanho)
    print(cadastro_valor)