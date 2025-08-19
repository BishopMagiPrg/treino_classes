class Carro:
    rodas = 4

    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

carro1 = Carro("Ford", "Focus", 2019)
carro2 = Carro("BMW", "X1", "2021")

print(carro1.rodas)
print(carro2.rodas)

Carro.rodas = 6

print(carro1.rodas)
print(carro2.rodas)