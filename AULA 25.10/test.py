class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    def MostrarCarro(self):
        print(f'Marca:{self.marca}, Modelo:{self.modelo}, Ano:{self.ano}')

carro1 = Carro("Honda", "Civic", "2020")
carro2 = Carro("Peugeot", "208", "2022")
carro3 = Carro("Ford", "Ka", "2013")
carro4 = Carro("Fiat", "Uno", "2009")


carro1.MostrarCarro()
carro2.MostrarCarro()
carro3.MostrarCarro()
carro4.MostrarCarro()
