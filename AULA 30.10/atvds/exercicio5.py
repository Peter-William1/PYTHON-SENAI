import os
os.system('cls')

class Cinema:
    def __init__(self, nome,capacidade,ingressos_vendidos):
        self.nome = nome
        self.capacidade = capacidade
        self.ingressos_vendidos = ingressos_vendidos

    def vender_ingressos(self,quantidade):
        print(f"Foram vendidos {quantidade} ingressos!")
        if quantidade <= self.capacidade:
            self.ingressos_vendidos += quantidade
        else: print("quantidade invalida!")
    def cancelar_venda(self, quantidade):
        print(f"Voce cancelou {quantidade} ingressos!")
        self.ingressos_vendidos -= quantidade
    def lugares_disponiveis(self):
        self.capacidade -= self.ingressos_vendidos
        print(f'Assento(s) disponiveis:{self.capacidade}')
        return self.capacidade
    
cinema = Cinema('Cinema Popular', 50, 20)
cinema.vender_ingressos(19)
cinema.cancelar_venda(3)
cinema.lugares_disponiveis()

    
