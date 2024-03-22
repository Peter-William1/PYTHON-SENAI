import os
from lista_db import Lista

os.system('cls')


lista = Lista()
run = True

while run:
    print('=-=-=-=-=-=-=+BEM VINDO!+=-=-=-=-=-=-=')
    
    op = int(input('Escolha uma Função:\n1)Inserir.    2)Listar.    3)Editar.    4)Remover.    5)Sair.\n'))
    
    if op == 1:
        os.system('cls')
        lista.Inserir()
    elif op == 2:
        os.system('cls')
        lista.listar()
    elif op == 3:
        os.system('cls')
        lista.editar()
    elif op == 4:
        lista.remover()
    elif op == 5:
        run = False
    else: print('Opção invalida')