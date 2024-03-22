import tkinter as tk 

 

#janela
janela= tk.Tk()
janela.title("Cauculadora")
cor = "#bfe3dc"
janela.config(bg=cor, height=500, width=500)

#login label
row, col = 1, 0
login_label = tk.Label(text="Email/Numero de celular:")



#senha label
senha_label = tk.Label(text="Senha:")


#login entry
login_entry= tk.Entry()

#senha entry
senha_entry = tk.Entry()

#Botao verify
botao_verify= tk.Button()


#Ordem .pack
login_label.pack()
login_entry.pack()
senha_label.pack()
senha_entry.pack()


janela.mainloop()