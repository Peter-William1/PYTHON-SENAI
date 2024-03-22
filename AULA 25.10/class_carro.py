class Carro:
    #Criar um metodo para exibir os atributos de um carro
    def exibirInformacoes(self):
        print(f'Marca:{self.marca}, Modelo:{self.modelo}, Ano:{self.ano}')


carro1= Carro() #Criando uma instancia da classe Objeto
carro1.marca = "VW"
carro1.modelo = "Gol"
carro1.ano = 2012



carro2 = Carro() #Criando outra instancia da classe Objeto
carro2.marca = "Ford"
carro2.modelo = "Fiesta"
carro2.ano = 2016

carro3= Carro() #Criando uma instancia da classe Objeto
carro3.marca = "Toyota"
carro3.modelo = "Corolla"
carro3.ano = 2015



carro4 = Carro() #Criando outra instancia da classe Objeto
carro4.marca = "Honda"
carro4.modelo = "Civic"
carro4.ano = 2011


carro1.exibirInformacoes()
carro2.exibirInformacoes()
carro3.exibirInformacoes()
carro4.exibirInformacoes()

