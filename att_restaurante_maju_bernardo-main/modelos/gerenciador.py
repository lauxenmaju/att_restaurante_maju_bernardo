# modelos/gerenciador_restaurantes.py

from modelos.restaurante1 import Restaurante

class GerenciadorRestaurantes:
    def __init__(self):
        self.restaurantes = []

    def adicionar_restaurante(self, nome, categoria, avaliacoes=None):
        novo_restaurante = Restaurante(nome, categoria, avaliacoes=avaliacoes)
        self.restaurantes.append(novo_restaurante)
        print(f'O restaurante {nome} foi cadastrado com sucesso')

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

    def receber_avaliacao(self, nome_restaurante, cliente, nota):
        for restaurante in self.restaurantes:
            if restaurante.nome == nome_restaurante:
                restaurante.adicionar_avaliacao(cliente, nota)
                print(f'Avaliação adicionada com sucesso ao restaurante {nome_restaurante}')
                return
        print('O restaurante não foi encontrado')

    def listar_avaliacoes_restaurante(self, nome_restaurante):
        for restaurante in self.restaurantes:
            if restaurante.nome == nome_restaurante:
                print(f'Avaliações do restaurante {nome_restaurante}:')
                print(restaurante.listar_avaliacoes())
                return
        print('O restaurante não foi encontrado')
