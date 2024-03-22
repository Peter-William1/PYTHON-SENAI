import os 
os.system('cls')

class Pessoa:
    def __init__(self, altura, idade, nome):
        self.altura = altura
        self.idade = idade
        self.nome = nome

    def falar(self):
        print(f"{self.nome} esta falando.")

    def aniversario(self):
        self.idade +=1
        print(f"Parabens {self.nome}!")

p1 = Pessoa("1.60m", 16,'peter')

p1.falar()
p1.aniversario()