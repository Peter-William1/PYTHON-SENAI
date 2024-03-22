import os 
os.system('cls')

class Carro:
    def __init__(self, marca, modelo, tanque_combustivel, consumo):
        self.marca = marca
        self.modelo = modelo
        self.tanque_combustivel = tanque_combustivel
        self.consumo = consumo
    def dirigir(self, distancia):
        self.tanque_combustivel -= distancia / self.consumo
        print(f"{self.tanque_combustivel}L")
    def abastacer(self, litros):
        if litros < 55: #capacidade media de um carro brasileiro
            self.tanque_combustivel += litros
        print(f"{self.tanque_combustivel}L")


carro = Carro("toyota", 'corola', 30, 19)

carro.dirigir(40)
carro.abastacer(20)