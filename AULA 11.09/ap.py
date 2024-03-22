lista= []
feitas= []
lista.append(input("Digite a Tarefa\n"))
for i in range(0,len(lista)):
    print("\nTarefas:\n", i + 1, ". ", lista[i])
for i in range(0,len(feitas)):
    print("\nFEITAS:\n", i + 1, ". ", feitas[i])
op=int(input("\nOque deseja fazer?\n1.Marcar uma tarefa como concluida 2.Adicionar outra tarefa"))
if op==1:
  op= int(input("Qual tarefa voce deseja marcar como concluida?"))
  feitas.append(lista[op-1])
  print(feitas)
elif op==2 :
  lista.append(input("Digite a Tarefa"))
elif op==3 :
   op= int(input("Qual tarefa deseja remover"))
   lista.pop(op)
for i in range(0,len(lista)):
    print(i + 1, ". ", lista[i])
for i in range(0,len(feitas)):
    print("\nFEITAS:\n", i + 1, ". ", feitas[i])