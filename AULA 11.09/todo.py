import os
lista= []

feitas= []
os.system("cls")
while(True): 
    if len(lista)<=0:
        print("Parece que nao temos nenhuma Tarefa!")  
        lista.append(input("Digite uma Tarefa\n"))
        os.system("cls")
    print("Tarefas:")
    for i in range(0,len(lista)):
        print(i + 1, ". ", lista[i])
    print("\nConcluidas:")
    if len(feitas)<=0:
        print("Nenhuma tarefa concluida!")  
    for i in range(0,len(feitas)):
        print( i + 1, ". ", feitas[i])
    op=int(input("\nOque deseja fazer?\n1.Marcar uma tarefa como concluida \n2.Adicionar outra tarefa\n3.Remover uma tarefa \n4.Limpar lista\n"))
    if op==1:
        op= int(input("Qual tarefa voce deseja marcar como concluida?"))
        feitas.append(lista[op-1])
        print(feitas)
    elif op==2 :
        lista.append(input("Digite a Tarefa: "))
    elif op==3 :
        op= int(input("Qual tarefa deseja remover"))
        lista.pop(op-1)
    elif op==4:
        os.system("cls")
        lista.clear()
        
 