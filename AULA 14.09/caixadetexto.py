import tkinter as tk

# Função para obter o texto da caixa de texto quando o botão é pressionado
def obter_texto():
    texto_digitado = caixa_texto.get()
    label_resultado.config(text="Texto digitado: " + texto_digitado)

# Cria a janela principal
janela = tk.Tk()
janela.title("Caixa de Texto Tkinter")

# Cria uma caixa de texto
caixa_texto = tk.Entry(janela, width=30)  # Defina a largura desejada
caixa_texto.pack()

# Cria um botão para obter o texto da caixa de texto
botao = tk.Button(janela, text="Obter Texto", command=obter_texto)
botao.pack()

# Rótulo para exibir o texto digitado
label_resultado = tk.Label(janela, text="")
label_resultado.pack()

# Inicia o loop principal do Tkinter
janela.mainloop()