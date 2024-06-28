class Avaliacao:
    def __init__(self, cliente, nota):
        self.cliente = cliente
        self.nota = nota

    def __str__(self):
        return f'Cliente: {self.cliente}, Nota: {self.nota}'