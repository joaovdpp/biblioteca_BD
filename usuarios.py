import sqlite3

with sqlite3.connect('biblioteca.db') as conexao:
    cursor = conexao.cursor()
    cursor.execute('CREATE TABLE if not exists Usuarios(id INTEGER PRIMARY KEY,nome TEXT)')
    
def adicionar_usuario():
    nome = input("Digite o nome do Usuário \n:")
    id = int(input("Digite o ID \n :"))
    dados = [id, nome]
    inserir_usuario(dados)

def inserir_usuario(dados):
    with sqlite3.connect('biblioteca.db') as conexao:
        cursor = conexao.cursor()
        inserir = 'INSERT INTO Usuarios VALUES(?, ?)'
        cursor.execute(inserir, dados)
        