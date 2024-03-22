import os
os.system("cls")

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario= salario
    def addAumento(self, valor):
        self.salario+= valor
    def ganhoAnual(self):
        return self.salario*12
    def exibe_dados(self):
        print(f"Nome:{self.nome}   Salario:{self.salario}")
        return self.nome, self.salario
    
class Assistente(Funcionario):
    def __init__(self, nome, salario, numero_de_matricula):
        super().__init__(nome, salario)
        self.numero_de_matricula = numero_de_matricula
    def exibe_dados(self):
        print(f"Nome:{self.nome}   Salario:{self.salario}    Numero de matricula:{self.numero_de_matricula}")
        return self.nome, self.salario
        
class Tecnicos(Assistente):
    def __init__(self, nome, salario, numero_de_matricula, bonus):
        super().__init__(nome, salario, numero_de_matricula)
        self.bonus = bonus
    def ganhoAnual(self):
        print(f'Ganho Anual de R$:{(self.salario+self.bonus)*12}')
class Administrativos(Assistente):
    def __init__(self, nome, salario, numero_de_matricula, turno, bonus_noturno):
        super().__init__(nome, salario, numero_de_matricula)
        self.turno= turno
        self.bonus_noturno = bonus_noturno
    def ganhoAnual(self):
        if self.turno == "noturno":
            print(f"ganho Anual de R$:{(self.salario+self.bonus_noturno)*12}")
        else: print(f'Ganho Anual de R$:{self.salario* 12}')


t1 = Tecnicos('Andre', 1200, 1341, 300)
t1.exibe_dados()
t1.ganhoAnual()

a1= Administrativos('Carlos', 1200, 4221, "noturno", 500)
a1.exibe_dados()
a1.ganhoAnual()