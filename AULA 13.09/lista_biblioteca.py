
def add(list):
    novo_contato =[]    
    nome=(input("digite o nome do contato:"))
    numero=input("digite o numero do contato:")
        
    novo_contato.append(nome)
    novo_contato.append(numero)
        
    list.append(novo_contato)

def ex(list):
    op=int(input("digite qual linha vai excluir:"))
    list.pop(op)

def listar(list):
    if len(list)>=1: 
        for i in range(0,len(list)):
          print(i+1,".", list[i][0], list[i][1])
    else: print("Não ha nenhum contato na agenda!")
    
def exlista(list):
    for i in range(0,len(list)): list.pop()

def edit(list):
    op=int(input("Digite numero do contato:"))
    i=int(input("1)Nome do contato\n2)Numero do contato\nVocê deseja editar:"))
    if i==1:
      nome=(input("digite o nome do contato editado:"))
      list[op][0]=nome
    if i==2:
      numero=input("digite o numero do contato editado:")
      list[op][1]=numero
    

