import sqlite3

with sqlite3.connect('biblioteca.db') as conexao:
    cursor = conexao.cursor()
    cursor.execute('CREATE TABLE if not exists Livros(id INTEGER PRIMARY KEY,nome TEXT, edicao TEXT, ano_publicacao INT, id_autor INT, id_editora INT, disponivel TEXT, CONSTRAINT fk_autor_livro FOREIGN KEY (id_autor) REFERENCES Autores(id), CONSTRAINT fk_editora_livro FOREIGN KEY (id_editora) REFERENCES Editoras(id) )')
    
def adicionar_livro():
    nome = input("Digite o Título do Livro \n : ")
    edicao = input("Defina a edição do Livro \n : ")
    ano_publicacao = int(input("Digite o ano de publicação do Livro \n :"))
    id = int(input("Digite o id do Livro \n :"))
    id_autor = int(input("Digite o ID do autor \n :"))
    id_editora = int(input("Digite o ID da editora \n:"))
    disponivel = input("O Livro está disponivel? (s/n) \n:")
    if disponivel == "s":
        disponivel = "Sim"
    elif disponivel == "n":
        disponivel = "Não"
    else: 
        print("erro! \n disponivel = indefinido")
        disponivel = "Indefinido"
    dados = [id, nome, edicao, ano_publicacao, id_autor , id_editora, disponivel]
    inserir_livro(dados)

def inserir_livro(dados):
    with sqlite3.connect('biblioteca.db') as conexao:
        cursor = conexao.cursor()
        inserir = 'INSERT INTO Livros VALUES(?, ?, ?, ?, ?, ?, ?)'
        cursor.execute(inserir, dados)
        