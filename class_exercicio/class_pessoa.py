class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentacao(self):
        print(f"Olá meu nome é {self.nome} e tenho {self.idade} anos.")


p1 = Pessoa("João",42)
p1.apresentacao()