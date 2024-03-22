import tkinter as tk 
import FIlasbibli as fl

#sistemas de filas
filas_paciente= [
    
    
]
fila_registro= []


#Janela inicial
janela= tk.Tk()
janela.title("Fila hospital")
cor='#252929'
janela.config(bg=cor)

def obter_conteudo():
    texto_da_caixa = inserir_nome_paciente.get() 
    filas_paciente.append(texto_da_caixa)
    print(texto_da_caixa)
    print(filas_paciente)
def exibir_fila():
    texto=""
    for i, item in enumerate(filas_paciente, start=1):
        texto += f"Paciente Nº{i}. {item}\n"
    
    label_fila.config(text=texto)

    

#Label para nome do paciented
nome_paciente= tk.Label(text="nome do paciente:")
nome_paciente.pack()
nome_paciente.place(x=30, y=30)

#Inserir nome dos pacientes
inserir_nome_paciente= tk.Entry(janela)
inserir_nome_paciente.pack()
inserir_nome_paciente.place(x=140, y=30)

#botao registrar
botao_registrar= tk.Button(janela, text="registrar", command=obter_conteudo)
botao_registrar.pack()
botao_registrar.place(x=300, y=30)

#botao exibir fila
botao_exibir_fila= tk.Button(janela, text="Exibir FIla", command=exibir_fila)
botao_exibir_fila.pack()

#label exibir fila

label_fila=tk.Label(janela, text=filas_paciente, width=60)
label_fila.pack()
label_fila.place(y=300)



janela.mainloop()