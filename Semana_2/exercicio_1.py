class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"{self.nome} ({self.idade} anos)"

p1 = Pessoa("Ana", 25)
p2 = Pessoa("João", 30)

print(p1)
print(p2)