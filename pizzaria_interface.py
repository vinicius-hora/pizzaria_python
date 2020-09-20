from PyQt5 import uic, QtWidgets

def mostrar_tela_venda():
    tela_venda.show()
    tela_pizzaria_venda.exec()


tela_inicial=QtWidgets.QApplication([])
tela_pizzaria = uic.loadUi("loja/tela_ini.ui")
tela_pizzaria_venda=QtWidgets.QApplication([])
tela_venda = uic.loadUi("loja/tela_venda.ui")
tela_pizzaria.cadastro_venda.triggered.connect(mostrar_tela_venda)



tela_pizzaria.show()
tela_inicial.exec()

