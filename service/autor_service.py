from dao.Autor_dao import AutorDAO
from model.Autor import Autor

class AutorService:

    def __init__(self):
        self.__autor_dao: AutorDAO = AutorDAO()

    @property
    def autor_dao(self) -> AutorDAO:
        return self.__autor_dao

    def menu(self):
        print('[Autores] Escolha uma das seguintes opções:\n'
                '1 - Listar todas os Autores\n'
                '2 - Adicionar novo Autor\n'
                '3 - Excluir Autor\n'
                '4 - Ver Autor por Id\n'
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
        print('\nListando Autores...')

        try:
            autores = self.__autor_dao.listar()
            if len(autores) == 0:
                print('Nenhuma editora encontrada!')

            for autor in autores:
                print(f'{autor.id} | {autor.nome}')
        except Exception as e:
            print(f'Erro ao exibir as Autores! - {e}')
            return

        input('Pressione uma tecla para continuar...')

    def adicionar(self):
        print('\nAdicionando Autor...')

        try:
            id = self.__autor_dao.ultimo_id() + 1
            nome = input('Digite o nome do Autor: ')
            email = input('Digite o endereço do Autor: ')
            telefone = input('Digite o telefone do Autor: ')
            bio = input('Digite a Bio do Autor: ')
            novo_autor = Autor(id, nome, email, telefone, bio)
            self.__autor_dao.adicionar(novo_autor)
            print('Autor adicionado com sucesso!')
        except Exception as e:
            print(f'Erro ao inserir Autor! - {e}')
            return

        input('Pressione uma tecla para continuar...')

    def remover(self):
        print('\nRemovendo Autor...')

        try:
            autor_id = int(input('Digite o ID do Autor para excluir: '))
            if (self.__autor_dao.remover(autor_id)):
                print('Autor excluída com sucesso!')
            else:
                print('Autor não encontrada!')
        except Exception as e:
            print(f'Erro ao excluir Autor! - {e}')
            return
        
        input('Pressione uma tecla para continuar...')

    def mostrar_por_id(self):
        print('\nAutor por Id...')

        try:
            id = int(input('Digite o Id do Autor para buscar: '))
            aut = self.__autor_dao.buscar_por_id(id)

            if (aut == None):
                print('Autor não encontrada!')
            else:
                print(f'Id: {aut.id} | Autor: {aut.nome}')    
        except Exception as e:
            print(f'Erro ao exibir Autor! - {e}')
            return     
        
        input('Pressione uma tecla para continuar...')