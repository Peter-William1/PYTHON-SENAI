import os 
os.system('cls')



#=-=-=-=-=[ATIVIDADE]=-=-=-=-=#

class Cliente:
    def __init__(self, saldo, nome):
        self.saldo = saldo 
        self.nome = nome

class Clienteouro(Cliente):
    def transferir(self,destino,valor):
        
        destino.saldo += valor
        self.saldo -= valor + 15 + (valor*0.02)

class Clienteprata(Cliente):
    def transferir(self,destino,valor):
       
        destino.saldo += valor
        self.saldo -= valor + 15 + (valor*0.05)

class Clientebronze(Cliente):
    def transferir(self,destino,valor):
        
        destino.saldo += valor
        self.saldo -= valor + 15 + (valor*0.10)
        


def tranferencia(origem,destino,valor):
    origem.transferir(destino,valor)
    print(f'{origem.nome} fez uma tranferencia de R$:{valor} para {destino.nome}!')
def exibir_saldo(origem):
    print(f"{origem.nome} tem um saldo de R$:{origem.saldo}")


#=-=-=-=-=[EXEMPLOS]=-=-=-=-=#

#--> CLIENTE UM FAZ UMA TRANSFERENCIA PARA CLIENTE 2
c1 = Clienteprata(5000, 'Andre')

c2 = Clienteouro(1000,'Paulo')

tranferencia(c1,c2, 3000)

#--> MOSTRANDO O SALDO DO CLIENTE 2, QUE RECEBEU A TRANSAÇÃO

exibir_saldo(c2)

# --> MOSTRANDO O SALDO DO CLIENTE UM, QUE FOI DESCONTADO PELA TRANSAÇÃO

exibir_saldo(c1)