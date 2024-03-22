import os
import lista_biblioteca as sistema
os.system("cls")
agenda =[
    
    
]


while (True):
    
    op=int(input("1)Adicionar um contato\n2)Editar um contato\n3)Listar agenda\n4)Excluir um contato\n5)Excluir agenda\nSelecione uma opção:"))
    if op==1:
        
        sistema.add(agenda)
        os.system("cls")
    if op==2:
        sistema.edit(agenda)
        os.system("cls")
    if op==3:
        sistema.listar(agenda)
    if op==4:
        sistema.ex(agenda)
        os.system("cls")
    if op==5:
        sistema.exlista(agenda)
        os.system("cls")
    if op==6:
        print(agenda)
        os.system("cls")