class Conta_bancaria:
    def __init__(self,titular,saldo):
        self.titular = titular
        self.saldo = saldo
    def depositar(self, valor_desejado):
        self.saldo += valor_desejado
        print(f'Você depositou R${valor_desejado}!')
    def sacar(self,valor_desejado):
        if valor_desejado >= self.saldo:
            self.saldo -= valor_desejado
            print(f'Você sacou R${valor_desejado}!')
        else : print('Valor de saque maior que o saldo!')

conta1= Conta_bancaria('Peter', 1000)

conta1.depositar(500)
conta1.sacar(1500)