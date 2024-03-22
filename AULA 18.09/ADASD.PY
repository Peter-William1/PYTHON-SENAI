import tkinter as tk
from tkinter import messagebox

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

class PilhaDeLivros:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def remover_livro(self):
        if not self.vazia():
            return self.livros.pop()
        else:
            raise IndexError("A pilha de livros está vazia")

    def ver_topo(self):
        if not self.vazia():
            return self.livros[-1]
        else:
            raise IndexError("A pilha de livros está vazia")

    def total_de_livros(self):
        return len(self.livros)

    def vazia(self):
        return len(self.livros) == 0

class BibliotecaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Biblioteca")

        self.biblioteca = {}
        self.pilha_selecionada = None

        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        self.label_genero = tk.Label(self.frame, text="Gênero:")
        self.label_genero.grid(row=0, column=0)

        self.entry_genero = tk.Entry(self.frame)
        self.entry_genero.grid(row=0, column=1)

        self.button_criar_pilha = tk.Button(self.frame, text="Criar Pilha", command=self.criar_pilha)
        self.button_criar_pilha.grid(row=0, column=2)

        self.button_listar_generos = tk.Button(self.frame, text="Listar Gêneros", command=self.listar_generos)
        self.button_listar_generos.grid(row=0, column=3)

        self.label_titulo = tk.Label(self.frame, text="Título:")
        self.label_titulo.grid(row=1, column=0)

        self.entry_titulo = tk.Entry(self.frame)
        self.entry_titulo.grid(row=1, column=1)

        self.label_autor = tk.Label(self.frame, text="Autor:")
        self.label_autor.grid(row=1, column=2)

        self.entry_autor = tk.Entry(self.frame)
        self.entry_autor.grid(row=1, column=3)

        self.button_adicionar_livro = tk.Button(self.frame, text="Adicionar Livro", command=self.adicionar_livro)
        self.button_adicionar_livro.grid(row=1, column=4)

        self.button_remover_livro = tk.Button(self.frame, text="Remover Livro", command=self.remover_livro)
        self.button_remover_livro.grid(row=2, column=4)

        self.button_ver_topo = tk.Button(self.frame, text="Ver Topo", command=self.ver_topo)
        self.button_ver_topo.grid(row=3, column=4)

        self.button_total_de_livros = tk.Button(self.frame, text="Total de Livros", command=self.total_de_livros)
        self.button_total_de_livros.grid(row=4, column=4)

        self.text_area = tk.Text(self.frame, height=10, width=40)
        self.text_area.grid(row=2, column=0, columnspan=4)

    def criar_pilha(self):
        genero = self.entry_genero.get()
        if genero:
            if genero not in self.biblioteca:
                self.biblioteca[genero] = PilhaDeLivros()
                self.text_area.insert(tk.END, f"Pilha para '{genero}' criada com sucesso!\n")
            else:
                messagebox.showinfo("Aviso", f"A pilha para '{genero}' já existe.")
        else:
            messagebox.showwarning("Aviso", "Digite um gênero válido.")

    def listar_generos(self):
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, "Gêneros disponíveis:\n")
        for genero in self.biblioteca:
            self.text_area.insert(tk.END, genero + "\n")

    def adicionar_livro(self):
        genero = self.entry_genero.get()
        titulo = self.entry_titulo.get()
        autor = self.entry_autor.get()

        if genero in self.biblioteca:
            livro = Livro(titulo, autor)
            self.biblioteca[genero].adicionar_livro(livro)
            self.text_area.insert(tk.END, f"O livro '{livro.titulo}' foi adicionado à pilha de '{genero}'.\n")
        else:
            messagebox.showwarning("Aviso", "O gênero não existe. Crie uma pilha para esse gênero primeiro.")

    def remover_livro(self):
        genero = self.entry_genero.get()

        if genero in self.biblioteca:
            try:
                livro = self.biblioteca[genero].remover_livro()
                self.text_area.insert(tk.END, f"O livro '{livro.titulo}' foi removido da pilha de '{genero}'.\n")
            except IndexError:
                self.text_area.insert(tk.END, f"A pilha de '{genero}' está vazia.\n")
        else:
            messagebox.showwarning("Aviso", "O gênero não existe. Crie uma pilha para esse gênero primeiro.")

    def ver_topo(self):
        genero = self.entry_genero.get()

        if genero in self.biblioteca:
            try:
                livro = self.biblioteca[genero].ver_topo()
                self.text_area.insert(tk.END, f"O livro no topo da pilha de '{genero}' é '{livro.titulo}' de '{livro.autor}'.\n")
            except IndexError:
                self.text_area.insert(tk.END, f"A pilha de '{genero}' está vazia.\n")
        else:
            messagebox.showwarning("Aviso", "O gênero não existe. Crie uma pilha para esse gênero primeiro.")

    def total_de_livros(self):
        genero = self.entry_genero.get()

        if genero in self.biblioteca:
            total = self.biblioteca[genero].total_de_livros()
            self.text_area.insert(tk.END, f"A pilha de '{genero}' contém {total} livro(s).\n")
        else:
            messagebox.showwarning("Aviso", "O gênero não existe. Crie uma pilha para esse gênero primeiro.")

if __name__ == "__main__":
    root = tk.Tk()
    app = BibliotecaApp(root)
    root.mainloop()
