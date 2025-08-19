class Carro:
    veiculo = "carro"

    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def apresentar(self):
        print(f"Este {Carro.veiculo} é um {self.marca} {self.modelo} de {self.ano}.")

c1 = Carro("Toyota", "Corola", "2020")
c2 = Carro("Honda", "Civic", "2022")

c1.apresentar()
c2.apresentar()
