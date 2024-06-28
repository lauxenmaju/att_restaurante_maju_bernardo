# modelos/restaurante.py

from modelos.avaliacao import Avaliacao

class Restaurante:
    def __init__(self, nome, categoria, ativo=False, avaliacoes=None):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.avaliacoes = avaliacoes if avaliacoes else []

    def alternar_estado(self):
        self.ativo = not self.ativo

    def adicionar_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self.avaliacoes.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self.avaliacoes:
            return '-'
        soma_das_notas = sum(avaliacao.nota for avaliacao in self.avaliacoes)
        quantidade_de_notas = len(self.avaliacoes)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media

    def listar_avaliacoes(self):
        if not self.avaliacoes:
            return 'Sem avaliações'
        return "\n".join(str(avaliacao) for avaliacao in self.avaliacoes)

    def __str__(self):
        estado = 'Ativo' if self.ativo else 'Desativado'
        media_avaliacoes = self.media_avaliacoes
        return f'{self.nome.ljust(20)} | {self.categoria.ljust(20)} | {estado} | Média Avaliações: {media_avaliacoes}'
