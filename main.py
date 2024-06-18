from modelos.restaurante import InterfaceUsuario

def main():
    app = InterfaceUsuario()

    app.gerenciador.adicionar_restaurante("Costa", "Comida Brasileira")
    app.gerenciador.adicionar_restaurante("Italian House", "Comida Italiana")
    app.gerenciador.adicionar_restaurante("La'Salvador", "Comida Mexicana")

    app.main()

if __name__ == '__main__':
    main()
