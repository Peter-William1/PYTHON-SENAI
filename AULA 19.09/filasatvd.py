import FIlasbibli as fl

loop=False

fila=[]
fila_registro= []
while loop==False:
    op=int (input("Oque deseja fazer?\n1)Registrar um paciente na fila  2)Chamar o próximo paciente    3)Mostrar os próximos N pacientes   4)Mostrar o total de pacientes na fila   5)Buscar um paciente pelo nome.\n"))
    if op==1:fl.add_paciente(fila, fila_registro)
    elif op==2:fl.chamar_um_paciente(fila)
    elif op==3:fl.mostrar_paciente(fila, fila_registro)
    elif op==4:fl.mostrar_total(fila)
    elif op==5:fl.buscar_paciente(fila)
    else: print("Opção nao encontrada!\nDigite novamnete!")