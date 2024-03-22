import tkinter as tk
from tkinter import PhotoImage

def change_image():
    global image_index
    image_index = (image_index + 1) % len(image_paths)
    new_image_path = image_paths[image_index]
    img = PhotoImage(file=new_image_path)
    button.config(image=img)
    button.image = img  # Manter uma referência para a imagem para evitar que ela seja coletada pelo garbage collector

# Lista de caminhos de imagem que você deseja alternar
image_paths = ["png-transparent-night-mode-icon-logo-switch-sun-on-off-digital-thumbnail1.png", "png-transparent-night-mode-icon-logo-moon-switch-on-off-digital-thumbnail.png"]
image_index = 0  # Índice da imagem atual

# Cria uma janela
root = tk.Tk()
root.title("Botão de Imagem Trocável")

# Carrega a primeira imagem da lista de caminhos
img = PhotoImage(file=image_paths[image_index])

# Cria um botão com a imagem inicial
button = tk.Button(root, image=img, command=change_image)
button.pack()

# Inicia a janela principal
root.mainloop()