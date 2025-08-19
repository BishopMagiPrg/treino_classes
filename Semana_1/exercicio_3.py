class Pessoa:
    total_pessoas = 0

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        Pessoa.total_pessoas += 1

p1 = Pessoa("Ana", 25)
p2 = Pessoa("João", 30)
p3 = Pessoa("Maria", 20)

print("Total de pessoas criadas:", Pessoa.total_pessoas)