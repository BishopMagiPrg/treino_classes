# treino_classes
## Semana 1 – Fundamentos de Classes
### Objetivos da Semana
- Entender o que é uma classe e uma instância.
- Criar atributos (características) e métodos (comportamentos).
- Diferenciar atributos de instância e atributos de classe.

### Aula Teórica (resumida)
- Classe → É como uma “planta” ou molde (define como os objetos devem ser).
- Instância → É um objeto concreto criado a partir da classe.
- Atributos → São as características (ex: nome, idade).
- Métodos → São as ações (ex: falar, andar).
- Atributos de Classe → Iguais para todas as instâncias.
- Atributos de Instância → Específicos de cada objeto.

### Exercícios da Semana
#### Exercício 1 – Primeira Classe

Cria uma classe Carro com:
- Atributos: marca, modelo, ano.
- Método: apresentar() que imprime algo como “Este carro é um Toyota Corolla de 2020”.
- Cria 2 carros diferentes e chama o método.

#### Exercício 2 – Atributos de Classe
Na classe Carro, adiciona um atributo de classe chamado rodas = 4.
- Imprime carro1.rodas e carro2.rodas.
- Depois altera Carro.rodas = 6 e verifica se mudou em todos os objetos.

#### Exercício 3 – Contador de Instâncias
Na classe Pessoa, cria um atributo de classe chamado total_pessoas = 0.
- Cada vez que crias uma nova Pessoa, incrementa esse contador.
- Mostra quantas pessoas foram criadas no final.
---

## Semana 2 – Métodos Especiais e Encapsulamento
### Objetivos da Semana
- Aprender a usar métodos especiais (__init__, __str__, __repr__).
- Entender o conceito de encapsulamento (proteger atributos).
- Praticar getters e setters.

### Teoria Rápida
#### Métodos Especiais
- __init__ → Construtor, chamado ao criar objeto.
- __str__ → Retorno quando usas print(obj).
- __repr__ → Retorno oficial (útil em debug, listas).

