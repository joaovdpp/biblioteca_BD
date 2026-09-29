import sqlite3 

with sqlite3.connect('biblioteca.db') as conexao:
    cursor = conexao.cursor()
    cursor.execute('CREATE TABLE if not exists emprestimos(id INT PRIMARY KEY, id_usuario INT, data TEXT, CONSTRAINT fk_usuario_emprestimo FOREIGN KEY (id_usuario) REFERENCES Usuarios(id) )')
    cursor.execute('CREATE TABLE if not exists emprestimos_livros(id_emprestimo INT, id_livro INT, data_devolucao TEXT, CONSTRAINT fk_emprestimo_livro FOREIGN KEY(id_emprestimo) REFERENCES emprestimos(id), CONSTRAINT fk_livro FOREIGN KEY (id_livro) REFERENCES Livros(id))')

def cadastrar_emprestimo():
    livro = int(input("Digite o ID do Livro \n :"))
    id_usuario = int(input("Digite o ID do Usuário \n :"))
    data = input("Digite a data do empréstimo \n EX:00/00/00 \n:")
    data_devolucao = input("Digite a data de devolução \n EX:00/00/00  \n : ")
    id = int(input("Digite o ID do empréstimo \n :"))
    dados = [id, id_usuario, data]
    dados2 = [id, livro, data_devolucao, ]
    with sqlite3.connect('biblioteca.db') as conexao:
        cursor = conexao.cursor()
        inserir = 'INSERT INTO emprestimos VALUES(?, ?, ?)'
        inserir2 = 'INSERT INTO emprestimos_livros VALUES(?, ?, ?)'
        cursor.execute(inserir, dados)
        cursor.execute(inserir2, dados2)