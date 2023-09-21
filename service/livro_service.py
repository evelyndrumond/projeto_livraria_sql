from dao.Livro_dao import LivroDAO
from model.Livro import Livro
from dao.Categoria_dao import CategoriaDAO
from model.Categoria import Categoria
from dao.Editora_dao import EditoraDAO
from model.Editora import Editora
from dao.Autor_dao import AutorDAO
from model.Autor import Autor

class LivroService:

    def __init__(self, categoria_dao: CategoriaDAO, editora_dao: EditoraDAO, autor_dao: AutorDAO):
        self.__livro_dao: LivroDAO = LivroDAO()
        self.__categoria_dao: CategoriaDAO = categoria_dao
        self.__editora_dao: EditoraDAO = editora_dao
        self.__autor_dao: AutorDAO = autor_dao
    def menu(self):
        print('[Livros] Escolha uma das seguintes opções:\n'
                '1 - Listar todos os Livros\n'
                '2 - Adicionar novo Livro\n'
                '3 - Excluir Livro\n'
                '4 - Ver Livro por Id\n'
                '0 - Voltar ao menu anterior\n')
        escolha = input('Digite a opção: ')

        if escolha == '0':
            return
        if escolha == '1':
            self.listar()
        elif escolha == '2':
            self.adicionar()
        elif escolha == '3':
            self.remover()
        elif escolha == '4':
            self.mostrar_por_id()
        else:
            print('Opção inválida! Por favor, tente novamente!')

        self.menu()

    def listar(self):
        print('\nListando Livros...')

        try:
            livros = self.__livro_dao.listar()
            if len(livros) == 0:
                print('Nenhum Livro encontrado!')

            for livro in livros:
                print(f'Id: {livro.id} | Título: {livro.titulo} | Resumo: {livro.resumo} | Ano: {str(livro.ano)} | Páginas: {str(livro.paginas)} | Isbn: {livro.isbn} | Categoria: {livro.categoria.nome} | Editora: {livro.editora.nome}  | Autor: {livro.autor.nome}')
        except Exception as e:
            print(f'Erro ao exibir os Livros! - {e}')
            return

        input('Pressione uma tecla para continuar...')

    def adicionar(self):
        print('\nAdicionando Livro...')

        try:
            id = self.__livro_dao.ultimo_id() + 1
            titulo = input('Digite o título do Livro: ')
            resumo = input('Digite o resumo do Livro: ')
            ano = int(input('Digite o ano do Livro: '))
            paginas = int(input('Digite o nº de páginas do Livro: '))
            isbn = input('Digite o isbn do Livro: ')
            
            print('Escolha a Categoria do Livro: ')
            lista_categoria = self.__categoria_dao.listar()
            for c in lista_categoria:
                print(f'{c.id} | {c.nome}')
            
            id_categoria = int(input('Digite o ID da categoria do livro: '))
            categoria: Categoria = self.__categoria_dao.buscar_por_id(id_categoria)

            while (categoria == None):
                print('Categoria não existente!')
                id_categoria = int(input('Digite o ID da categoria do livro: '))
                categoria: Categoria = self.__categoria_dao.buscar_por_id(id_categoria)

            print('Escolha a Editora do Livro: ')
            lista_editora = self.__editora_dao.listar()
            for e in lista_editora:
                print(f'{e.id} | {e.nome}')

            id_editora = int(input('Digite o ID da Editora do livro: '))
            editora: Editora = self.__editora_dao.buscar_por_id(id_editora)
            while (editora == None):
                print('Editora não existente!')
                id_editora = int(input('Digite o ID da editora do livro: '))
                editora: Editora = self.__editora_dao.buscar_por_id(id_editora)
            
            
            print('Escolha o Autor do Livro: ')
            lista_autor = self.__autor_dao.listar()
            for a in lista_autor:
                print(f'{a.id} | {a.nome}')
            
            id_autor = int(input('Digite o ID do Autor do livro: '))
            autor: Autor = self.__autor_dao.buscar_por_id(id_autor)

            while(autor == None):
                print('Autor não existente!')
                id_autor = int(input('Digite o ID do autor do livro: '))
                autor: Autor = self.__autor_dao.buscar_por_id(id_autor)

            novo_livro = Livro(id, titulo, resumo, ano, paginas, isbn, categoria, editora, autor)
            self.__livro_dao.adicionar(novo_livro)
            print('Livro adicionado com sucesso!')
        except Exception as e:
            print(f'Erro ao inserir Livro! - {e}')
            return

        input('Pressione uma tecla para continuar...')

    def remover(self):
        print('\nRemovendo Livro...')

        try:
            livro_id = int(input('Digite o ID do Livro para excluir: '))
            if (self.__livro_dao.remover(livro_id)):
                print('Livro excluído com sucesso!')
            else:
                print('Livro não encontrado!')
        except Exception as e:
            print(f'Erro ao excluir Livro! - {e}')
            return
        
        input('Pressione uma tecla para continuar...')

    def mostrar_por_id(self):
        print('\nLivro por Id...')

        try:
            id = int(input('Digite o Id do livro para buscar: '))
            liv = self.__livro_dao.buscar_por_id(id)

            if (liv == None):
                print('Livro não encontrado!')
            else:
                print(f'Id: {liv.id} | Título: {liv.titulo} | Resumo: {liv.resumo} | Ano: {str(liv.ano)} | Páginas: {str(liv.paginas)} | Isbn: {liv.isbn} | Categoria: {liv.categoria.nome}  | Editora: {liv.editora.nome}  | Autor: {liv.autor.nome}')
        except Exception as e:
            print(f'Erro ao exibir Livro! - {e}')
            return     
        
        input('Pressione uma tecla para continuar...')