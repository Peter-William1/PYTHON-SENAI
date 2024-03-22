import os
import pygame as pg
import random as r 

class Personagem():
    def __init__(self):
        self.x = 0
        self.y= 0
        self.points= 0
        self.tentou_sair = False
    def Mover_direita(self):
        if self.x < 2:
            self.x += 1
            self.points += 5
        else : self.tentou_sair = True

    def Mover_esquerda(self):
        if self.x >0:
            self.x -= 1 
            self.points += 5
        else : self.tentou_sair = True
    def Mover_baixo(self):
        if self.y <2:
            self.y += 1
            self.points += 5
        else : self.tentou_sair = True
    def Mover_cima(self):
        if self.y >0:
            self.y -= 1
            self.points += 5
        else : self.tentou_sair = True
    
    def status(self):
        if self.tentou_sair == True:
            self.x=0
            self.y=0
            self.points = 0
            self.tentou_sair = False
        print(f'Posicao atual:{self.x},{self.y}\npontuacao:{self.points}')
    def pos(self):
        return self.x
    def posy(self):
        return self.y

class inimigo():
    def __init__(self):
        self.y = r.randint(0, 2)
        self.x =  r.randint(0, 2)
    def posx(self):
        return self.x
    def posy(self):
        return self.y
        
def colisao(x,y,xx,yy):
    if x == xx and y== yy:
        return True
    else :return False

mapa = [["X", "X", "X"],
        ["X", "X", "X"],
        ["X", "X", "X"]]
        
inimigo1= inimigo()
personagem1 = Personagem()
os.system("cls")

while True:
    personagem1.status()

    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if personagem1.posy() == i and personagem1.pos() == j:
                print("O", end=' ')
            
            elif inimigo1.posy() == i and inimigo1.posx() == j:
                print("@", end=' ')
            else: print(mapa[i][j], end=" ")
        print()
            
    if colisao(personagem1.pos(), personagem1.posy(), inimigo1.posx(), inimigo1.posy()):
        print("colidiu")
        inimigo1= inimigo()
            
    op = input('Digite: "A" para esquerda, "S" para baixo, "D" para a direita e "W" para cima:\n ')
    
    if op == 'a':
         personagem1.Mover_esquerda()
    elif op == 's':
         personagem1.Mover_baixo()
    elif op == 'd':
         personagem1.Mover_direita()
    elif op == 'w':
         personagem1.Mover_cima()
    elif op == 'q':
         break

