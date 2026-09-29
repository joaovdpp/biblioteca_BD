import sqlite3

with sqlite3.connect('biblioteca.db') as conexao:
    cursor = conexao.cursor()
    cursor.execute('CREATE TABLE if not exists Editoras(id INTEGER PRIMARY KEY,nome TEXT)')
    
def adicionar_editora():
    nome = input(":")
    id = int(input(":"))
    dados = [id, nome]
    inserir_editora(dados)

def inserir_editora(dados):
    with sqlite3.connect('biblioteca.db') as conexao:
        cursor = conexao.cursor()
        inserir = 'INSERT INTO Editoras VALUES(?, ?)'
        cursor.execute(inserir, dados)
