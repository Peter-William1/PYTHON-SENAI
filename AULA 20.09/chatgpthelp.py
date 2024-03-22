import tkinter as tk

# Função para ler e exibir o conteúdo do arquivo de texto
def ler_arquivo():
    try:
        # Caminho do arquivo de texto
        caminho_arquivo = "arquivotexto.txt"

        # Abre o arquivo e lê o conteúdo
        with open(caminho_arquivo, "r") as arquivo:
            conteudo = arquivo.read()
            texto.configure(state="normal")  # Habilita a edição do widget de texto
            texto.delete("1.0", "end")  # Limpa qualquer conteúdo anterior
            texto.insert("1.0", conteudo)  # Insere o conteúdo do arquivo no widget de texto
            texto.configure(state="disabled")  # Desabilita a edição do widget de texto
    except FileNotFoundError:
        texto.configure(state="normal")  # Habilita a edição do widget de texto
        texto.delete("1.0", "end")  # Limpa qualquer conteúdo anterior
        texto.insert("1.0", "Arquivo não encontrado.")  # Exibe mensagem de erro
        texto.configure(state="disabled")  # Desabilita a edição do widget de texto

# Cria a janela principal
janela = tk.Tk()
janela.title("Leitor de Arquivo de Texto")

# Cria um botão para ler o arquivo de texto
botao_ler = tk.Button(janela, text="Ler Arquivo de Texto", command=ler_arquivo)
botao_ler.pack()

# Cria um widget de texto para exibir o conteúdo do arquivo
texto = tk.Text(janela, state="disabled", wrap=tk.WORD)
texto.pack()

# Inicia a interface gráfica
janela.mainloop()