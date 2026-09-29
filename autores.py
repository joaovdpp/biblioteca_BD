import sqlite3

with sqlite3.connect('biblioteca.db') as conexao:
    cursor = conexao.cursor()
    cursor.execute('CREATE TABLE if not exists Autores(id INTEGER PRIMARY KEY,nome TEXT)')
    
def adicionar_autor():
    nome = input(":")
    id = int(input(":"))
    dados = [id, nome]
    inserir_autor(dados)

def inserir_autor(dados):
    with sqlite3.connect('biblioteca.db') as conexao:
        cursor = conexao.cursor()
        inserir = 'INSERT INTO Autores VALUES(?, ?)'
        cursor.execute(inserir, dados)
   

