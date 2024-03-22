import os 
os.system('cls')

#=-=-=-=-=-=-=-+[codigo]+-=-=-=-=-=-=-=#

class Forma_geometrica:
    def area(self): return NotImplementedError('Subclasse deve implementar metodo abstrato')

class Retangulo(Forma_geometrica):
    def area(self):
        return self.base * self.altura 

class Triangulo(Forma_geometrica):
    def area(self):
        return (self.base * self.altura )/2

class Circulo(Forma_geometrica):
    def area(self):
        return 3.14 * (self.raio**2)
        

retangulo = Retangulo()

retangulo.base= 3
retangulo.altura= 5
retangulo.area()

triangulo = Triangulo()
triangulo.base = 5
triangulo.altura = 6
triangulo.area()

circulo = Circulo()
circulo.raio = 5
circulo.area()

def caucularArea(forma):
    print(forma.area())


caucularArea(triangulo)