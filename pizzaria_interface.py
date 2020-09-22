from PyQt5 import uic, QtWidgets
from datetime import datetime

#funçoes da tela de venda
def mostrar_tela_venda():
    tela_venda.show()
    tela_pizzaria_venda.exec()

def fechar_tela_venda():
    tela_venda.pack()
    tela_pizzaria_venda.exec()

def cadastrar_venda():
    cadastro_sabor = tela_venda.venda_sabor_text.text()
    cadastro_tamanho = tela_venda.venda_tamanho_text.text()
    cadastro_valor = tela_venda.valor_text.text()
    cadastro_data = datetime.today()

    #campos em branco
    tela_venda.venda_sabor_text.clear()
    tela_venda.venda_tamanho_text.clear()
    tela_venda.valor_text.clear()

    #impressao dos dados
    print(cadastro_sabor)
    print(cadastro_tamanho)
    print(cadastro_valor)
    print(cadastro_data)

#funções da tela de compra
def mostrar_tela_compra():
    tela_compra.show()
    tela_pizzaria_compra.exec()

def cadastrar_compra():
    cadastro_item = tela_compra.lineEdit_compra_item.text()
    cadastro_valor = tela_compra.doubleSpinBox_compra_valor.text()
    cadastro_data = datetime.today()

    #campos em branco
    tela_compra.lineEdit_compra_item.clear()
    tela_compra.doubleSpinBox_compra_valor.clear()

    #impressao teste
    print(cadastro_item)
    print(cadastro_valor)
    print(cadastro_data)





#Carregamento da tela inicial
tela_inicial=QtWidgets.QApplication([])
tela_pizzaria = uic.loadUi("loja/tela_ini.ui")
#Carregamento da tela de venda
tela_pizzaria_venda=QtWidgets.QApplication([])
tela_venda = uic.loadUi("loja/tela_venda.ui")
#Carregamento da tela de compra
tela_pizzaria_compra=QtWidgets.QApplication([])
tela_compra = uic.loadUi("loja/tela_compra.ui")

#Botões da tela inicial
tela_pizzaria.cadastro_venda.triggered.connect(mostrar_tela_venda)
tela_pizzaria.cadastro_compra.triggered.connect(mostrar_tela_compra)

#Botões da tela de venda
tela_venda.pushButton_cadastrar.clicked.connect(cadastrar_venda)
tela_venda.pushButton_cancelar.clicked.connect(tela_venda.close)

#botões tela de compra
tela_compra.pushButton_comprar.clicked.connect(cadastrar_compra)
tela_compra.pushButton_cancelar_compra.clicked.connect(tela_compra.close)







tela_pizzaria.show()
tela_inicial.exec()

