import tkinter as tk

# Função para adicionar dígitos à entrada
def adicionar_digito(digito):
    entrada.insert(tk.END, digito)

# Função para calcular o resultado
def calcular():
    try:
        expressao = entrada.get()
        resultado = eval(expressao)
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except Exception:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Erro")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Calculadora")

# Entrada de texto para a expressão
entrada = tk.Entry(janela, width=20)
entrada.grid(row=0, column=0, columnspan=4)

# Criação dos botões para os dígitos e operações
botoes = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

# Organização dos botões na janela
row, col = 1, 0
for botao in botoes:
    tk.Button(janela, text=botao, width=5, height=2, command=lambda b=botao: adicionar_digito(b) if b != "=" else calcular()).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Executa a interface gráfica
janela.mainloop()
