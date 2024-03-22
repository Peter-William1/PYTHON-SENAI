import os
def add_paciente(fila, fila_registro):
    pacientes=input("digite o nome do paciente:")
    numero_de_registro=input("Digite o numero de registo do paciente:")
    fila.append(pacientes)
    fila_registro.append(numero_de_registro)
    
    
def chamar_um_paciente(lista):
    
    paciente_chamado=lista.pop(0)
    print("Paciente chamado:", paciente_chamado)

def mostrar_paciente(lista,fila_registro):
    for i in range(0, len(lista)):
        print("Paciente Nº", i+1, ": ", lista[i])
        print("Nº de registro:", fila_registro[i], "\n")
def mostrar_total(lista):
    n= len(lista)
    print("Existem,", n, "pacientes na fila")

def buscar_paciente(lista, fila_registro):
    nome=input("digite o nome do paciente:")
    if nome in lista:
        posiçao= lista.index(nome)
        print("Paciente Nº:", posiçao+1, "Nº de registro:", fila_registro[posiçao])
    else :
        print("nenhum paciente com este nome encontrado!")

