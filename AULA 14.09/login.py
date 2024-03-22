import tkinter as tk



fonte= ("Comic Sans MS", 15)
# Função para obter o texto da caixa de texto quando o botão é pressionado
def obter_texto():
    
    senha_digitado = caixa_texto_senha.get()
    label_resultado_senha.config(text="Texto digitado: " + senha_digitado)
    

def cadastro():
    user = caixa_texto.get()
    senha = caixa_texto_senha.get()

    if (user)=="admin" and (senha)=="1234":
        label_resultado_senha.config(foreground="green")
        label_resultado_senha.config(text="fazendo login...")
    else:
        label_resultado_senha.config(foreground="red")
        label_resultado_senha.config(text="Verifique user e senha")
def whitemode():
    estado_atual= switch.get()
   
    print(estado_atual)
    if (estado_atual)==True:
        caixa_texto.config(bg=white, foreground=cor)
        inserir_senha.config(bg=white, foreground=cor)
        janela.config(bg=white)
        inserir_user.config(bg=white, foreground=cor)
        caixa_texto_senha.config(bg=white, foreground=cor)
        label_resultado_senha.config(bg=white)
        botao.config(bg=white, foreground=cor)
        botao2.config(text="Dark Mode", bg=white, foreground=cor)
       
    
    else:
        caixa_texto.config(bg=cor, foreground=cor)
        inserir_senha.config(bg=cor, foreground=white)
        janela.config(bg=cor)
        inserir_user.config(bg=cor, foreground=white)
        caixa_texto_senha.config(bg=cor, foreground=cor)
        label_resultado_senha.config(bg=cor)
        botao.config(bg=cor, foreground=white)
        botao2.config(text="White Mode", foreground=white, bg=cor)
    
       



# Cria a janela principal
white="#fafcfc"
janela = tk.Tk()
janela.title("Caixa de Texto Tkinter")
cor="#032e2e"
janela.config(bg=cor)


# Rótulo para exibir o user:
inserir_user = tk.Label(janela, text="User:", font=fonte)
inserir_user.pack()
inserir_user.config(bg=cor, foreground=white)

# Cria uma caixa de texto

caixa_texto = tk.Entry(janela, width=30)  # Defina a largura desejada
caixa_texto.pack()
caixa_texto.config(bg=cor)

# Rotulo para a senha
inserir_senha = tk.Label(janela, text="Senha:", font=fonte)
inserir_senha.pack()
inserir_senha.config(bg=cor, foreground=white)


# Cria uma caixa de texto
caixa_texto_senha = tk.Entry(janela, width=30)  # Defina a largura desejada
caixa_texto_senha.pack()
caixa_texto_senha.config(bg=cor)

# Cria um botão para obter o texto da caixa de texto
switch=tk.BooleanVar()
botao = tk.Button(janela, text="Entrar", command=cadastro)
botao.pack()
botao2 = tk.Checkbutton(janela, text="White Mode", variable=switch, command=whitemode, bg=cor, foreground=white)
botao2.pack()
botao.config(bg=cor, foreground=white)


# Rótulo para exibir a senha digitado
label_resultado_senha = tk.Label(janela, text="")
label_resultado_senha.pack()
label_resultado_senha.config(bg=cor)

inserir_user.place(x=10, y=1)
inserir_senha.place(x=10, y=40)
caixa_texto.place(x=80, y=10)
caixa_texto_senha.place(x=82, y=50)
botao.place(x=150, y= 100)
label_resultado_senha.place(x=150, y= 130)
botao2.place(x=1, y=300)

# Inicia o loop principal do Tkinter
janela.mainloop()