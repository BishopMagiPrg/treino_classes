class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self._idade = idade

    def get_idade(self):
        return self._idade
    
    def set_idade(self, nova_idade):
        if nova_idade >= 0:
            self._idade = nova_idade
        else: print("Idade inválida!")

p1 = Pessoa("João", 30)
print("Idade:", p1._idade)

p1.set_idade(35)
print("Idade:", p1.get_idade())

p1.set_idade(-5)
