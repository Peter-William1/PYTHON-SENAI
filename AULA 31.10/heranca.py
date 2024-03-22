import os
os.system('cls')

class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo 
    def ligar(self): print(f'O {self.modelo} esta ligado')
    def desligar(self): print(f'O {self.modelo} esta delisgado')
    

class Carro(Veiculo):
    def __init__(self, marca, modelo, numero_de_portas):
        super().__init__(marca, modelo)
        self.numero_de_portas = numero_de_portas
    def abastecer(self):
        print(f"o {self.modelo} esta sendo abastecido")
class Moto(Veiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
    def empinar(self):print("a moto esta empinando!")
class Carro_eletrico(Carro):
    def __init__(self, marca, modelo, numero_de_portas, bateria):
        super().__init__(marca, modelo, numero_de_portas)
    def recarregar_bateria(self):
        print(f"O {self.modelo} esta sendo carregado!")

c1 = Carro("Honda",'Civic', 4)

c1.ligar()
c1.desligar()

m1 = Moto("Yahama", 'Sahara')
m1.ligar()
m1.empinar()

c2 = Carro_eletrico('Tesla', 'Tesla 1', 4, 100)
c2.recarregar_bateria()
