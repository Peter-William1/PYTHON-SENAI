import tkinter as tk

# Função para alternar o estado do botão
def alternar_estado():
    estado_atual = botao_var.get()
    botao_var.set(not estado_atual)  # Inverte o valor do botão

# Cria a janela principal
janela = tk.Tk()
janela.title("Botão de Interruptor Tkinter")

# Cria uma variável de controle booleana
botao_var = tk.BooleanVar()

# Cria o botão de interruptor
botao = tk.Checkbutton(janela, text="Ligado/Desligado", variable=botao_var, command=alternar_estado)
botao.pack()

# Inicia o loop principal do Tkinter
janela.mainloop()