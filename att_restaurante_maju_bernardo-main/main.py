# main.py

from modelos.interface import InterfaceUsuario
from modelos.avaliacao import Avaliacao

def main():
    app = InterfaceUsuario()

    # Adicionando restaurantes predefinidos
    app.gerenciador.adicionar_restaurante('DI ZE', 'Italiana', avaliacoes=[Avaliacao('Carlos', 4), Avaliacao('Manu', 5)])
    app.gerenciador.adicionar_restaurante('Océan', 'Japonesa',  avaliacoes=[Avaliacao('Ana', 5), Avaliacao('João', 4)])
    app.gerenciador.adicionar_restaurante('Da terra', 'Brasileira',  avaliacoes=[Avaliacao('Pedro', 3), Avaliacao('Maria', 4)])

    app.main()

if __name__ == "__main__":
    main()
