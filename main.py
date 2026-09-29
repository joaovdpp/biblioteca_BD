from autores import adicionar_autor, inserir_autor
from livros import adicionar_livro
from usuarios import adicionar_usuario
from editoras import adicionar_editora
from emprestimo import cadastrar_emprestimo
while(True):
    menu = int(input("-----MENU----- " \
    "\n CADASTRAR EMPRÉSTIMO [1] CADASTRAR DEVOLUÇÃO [2] " \
    "\n ADICIONAR AUTOR [3] ADICIONAR USUÁRIO "
    "[4] \n ADICIONAR EDITORA [5] ADICIONAR LIVRO [6] \n : "))
    if menu == 1:
        cadastrar_emprestimo()
    elif menu == 3:
        adicionar_autor()
    elif menu == 4:
        adicionar_usuario()
    elif menu == 5:
        adicionar_editora()
    elif menu == 6:
        adicionar_livro()

