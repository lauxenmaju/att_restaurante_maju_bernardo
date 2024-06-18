import os

class Restaurante:
    def __init__(self, nome, categoria, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo

    def alternar_estado(self):
        self.ativo = not self.ativo

    def __str__(self):
        estado = 'Ativo' if self.ativo else 'Desativado'
        return f'{self.nome.ljust(20)} | {self.categoria.ljust(20)} | {estado}'
    
class GerenciadorRestaurantes:
    def __init__(self):
        self.restaurantes = []

    def adicionar_restaurante(self, nome, categoria):
        novo_restaurante = Restaurante(nome, categoria)
        self.restaurantes.append(novo_restaurante)
        print(f'O restaurante {nome} foi cadastrado com sucesso\n')

    def listar_restaurantes(self):
        print("Listando os restaurantes:\n")
        print(f'-Nome do Restaurante'.ljust(24), '-Categoria'.ljust(20), '-Ativo')
        for i, restaurante in enumerate(self.restaurantes):
            if i < 10 or len(self.restaurantes) <= 10:
                print(f'-{restaurante}')
        print("\nTotal de restaurantes cadastrados:", len(self.restaurantes))

    def alternar_estado_restaurante(self, nome):
        for restaurante in self.restaurantes:
            if restaurante.nome == nome:
                restaurante.alternar_estado()
                estado = 'ativado' if restaurante.ativo else 'desativado'
                print(f'O restaurante {nome} foi {estado} com sucesso')
                return
        print('O restaurante não foi encontrado')


class InterfaceUsuario:
    def __init__(self):
        self.gerenciador = GerenciadorRestaurantes()

    def mostrar_subtitulo(self, texto):
        os.system('clear')
        linha = '*' * len(texto)
        print(linha)
        print(texto)
        print(linha)
        print()

    def finalizar_app(self):
        self.mostrar_subtitulo('Finalizando o aplicativo')
        exit()

    def chamar_nome_do_app(self):
        print('''
        ℜ𝔢𝔰𝔱𝔞𝔲𝔯𝔞𝔫𝔱𝔢 𝔈𝔵𝔭𝔯𝔢𝔰𝔰𝔬
        ''')

    def voltar_ao_menu_principal(self):
        input('\nDigite uma tecla para voltar ao menu principal')
        self.main()

    def opcao_invalida(self):
        print('Opção inválida\n')
        self.voltar_ao_menu_principal()

    def exibir_opcoes(self):
        print("1 Cadastrar Restaurante")
        print("2 Listar Restaurante")
        print("3 Ativar/Desativar Restaurante")
        print("4 Sair\n")

    def cadastrar_novo_restaurante(self):
        os.system('clear')
        nome_do_restaurante = input('Digite o nome do novo restaurante: ')
        categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
        self.gerenciador.adicionar_restaurante(nome_do_restaurante, categoria)
        self.voltar_ao_menu_principal()

    def listar_restaurantes(self):
        self.mostrar_subtitulo('Listando os restaurantes')
        self.gerenciador.listar_restaurantes()
        self.voltar_ao_menu_principal()

    def alterar_estado_restaurante(self):
        self.mostrar_subtitulo('Alternando o estado do restaurante')
        nome_restaurante = input('Digite o nome do restaurante que desejas alternar o estado: ')
        self.gerenciador.alternar_estado_restaurante(nome_restaurante)
        self.voltar_ao_menu_principal()

    def escolher_opcao(self):
        try:
            opcao_digitada = int(input("Escolha uma opção: "))
            print("Você selecionou:", opcao_digitada, "\n")
            if opcao_digitada == 1:
                self.cadastrar_novo_restaurante()
            elif opcao_digitada == 2:
                self.listar_restaurantes()
            elif opcao_digitada == 3:
                self.alterar_estado_restaurante()
            elif opcao_digitada == 4:
                self.finalizar_app()
            else:
                self.opcao_invalida()
        except ValueError:
            self.opcao_invalida()

    def main(self):
        os.system('clear')
        self.chamar_nome_do_app()
        self.exibir_opcoes()
        self.escolher_opcao()


