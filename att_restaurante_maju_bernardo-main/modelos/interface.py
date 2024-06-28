# modelos/interface_usuario.py

import os
from modelos.gerenciador import GerenciadorRestaurantes
from modelos.avaliacao import Avaliacao

class InterfaceUsuario:
    def __init__(self):
        self.gerenciador = GerenciadorRestaurantes()

    def mostrar_subtitulo(self, texto):
        os.system('cls' if os.name == 'nt' else 'clear')
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
        print("2 Listar Restaurantes")
        print("3 Ativar/Desativar Restaurante")
        print("4 Avaliar Restaurante")
        print("5 Listar Avaliações de um Restaurante")
        print("6 Sair\n")

    def cadastrar_novo_restaurante(self):
        os.system('cls' if os.name == 'nt' else 'clear')
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
        nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
        self.gerenciador.alternar_estado_restaurante(nome_restaurante)
        self.voltar_ao_menu_principal()

    def avaliar_restaurante(self):
        self.mostrar_subtitulo('Avaliando restaurante')
        nome_restaurante = input('Digite o nome do restaurante que deseja avaliar: ')
        cliente = input('Digite o nome do cliente: ')
        try:
            nota = float(input('Digite a nota (0-5): '))
            self.gerenciador.receber_avaliacao(nome_restaurante, cliente, nota)
        except ValueError:
            print('Nota inválida')
        self.voltar_ao_menu_principal()

    def listar_avaliacoes_restaurante(self):
        self.mostrar_subtitulo('Listando avaliações de um restaurante')
        nome_restaurante = input('Digite o nome do restaurante que deseja ver as avaliações: ')
        self.gerenciador.listar_avaliacoes_restaurante(nome_restaurante)
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
                self.avaliar_restaurante()
            elif opcao_digitada == 5:
                self.listar_avaliacoes_restaurante()
            elif opcao_digitada == 6:
                self.finalizar_app()
            else:
                self.opcao_invalida()
        except ValueError:
            self.opcao_invalida()

    def main(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.chamar_nome_do_app()
        self.exibir_opcoes()
        self.escolher_opcao()
