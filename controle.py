from PyQt5 import uic, QtWidgets
import mysql.connector
conexao = mysql.connector.connect(
    
    host = '127.0.0.1',
    user = 'root',
    password = '',
    database = 'cadastro_produtos'
)
def inserir():
    produto = formulario.txtProduto.text()
    preco = formulario.txtPreco.text()
    estoque = formulario.txtEstoque()

    cursor = conexao.cursor()
    comando_SQL = 'INSERT INTO produtos (produto, preco, estoque) VALUES (%s,%s,%s)'
    dados = (produto, preco, estoque)
    cursor.execute(comando_SQL, dados)
    conexao.commit()

app=QtWidgets.QApplication([])
formulario=uic.loadUi('formulario.ui')
formulario.btnCadastrar.clicked.connect(inserir)

formulario.show()
app.exec()


