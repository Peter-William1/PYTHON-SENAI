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

class Biblioteca:
    def __init__(self):
        self.pilhas = {}  # Dicionário para mapear gêneros para as pilhas de livros

    def criar_pilha_para_genero(self, genero):
        if genero not in self.pilhas:
            self.pilhas[genero] = PilhaDeLivros()
        else:
            print(f"A pilha para o gênero '{genero}' já existe.")

    def listar_generos_disponiveis(self):
        print("Gêneros disponíveis:")
        for genero in self.pilhas:
            print(genero)

    def adicionar_livro_a_pilha(self, genero, livro):
        if genero in self.pilhas:
            self.pilhas[genero].adicionar_livro(livro)
            print(f"O livro '{livro.titulo}' foi adicionado à pilha de '{genero}'.")
        else:
            print(f"O gênero '{genero}' não existe. Crie uma pilha para esse gênero primeiro.")

    def remover_livro_da_pilha(self, genero):
        if genero in self.pilhas:
            try:
                livro = self.pilhas[genero].remover_livro()
                print(f"O livro '{livro.titulo}' foi removido da pilha de '{genero}'.")
                return livro
            except IndexError:
                print(f"A pilha de '{genero}' está vazia.")
        else:
            print(f"O gênero '{genero}' não existe. Crie uma pilha para esse gênero primeiro.")

    def ver_topo_da_pilha(self, genero):
        if genero in self.pilhas:
            try:
                livro = self.pilhas[genero].ver_topo()
                print(f"O livro no topo da pilha de '{genero}' é '{livro.titulo}' de '{livro.autor}'.")
            except IndexError:
                print(f"A pilha de '{genero}' está vazia.")
        else:
            print(f"O gênero '{genero}' não existe. Crie uma pilha para esse gênero primeiro.")

    def total_de_livros_na_pilha(self, genero):
        if genero in self.pilhas:
            total = self.pilhas[genero].total_de_livros()
            print(f"A pilha de '{genero}' contém {total} livro(s).")
        else:
            print(f"O gênero '{genero}' não existe. Crie uma pilha para esse gênero primeiro.")

def main():
    biblioteca = Biblioteca()

    while True:
        print("Opções:")
        print("1. Criar uma nova pilha para um gênero")
        print("2. Listar gêneros disponíveis")
        print("3. Adicionar livro a uma pilha")
        print("4. Remover livro de uma pilha")
        print("5. Ver livro no topo de uma pilha")
        print("6. Ver total de livros em uma pilha")
        print("7. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            genero = input("Digite o nome do gênero: ")
            biblioteca.criar_pilha_para_genero(genero)
        elif opcao == "2":
            biblioteca.listar_generos_disponiveis()
        elif opcao == "3":
            genero = input("Digite o nome do gênero: ")
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            livro = Livro(titulo, autor)
            biblioteca.adicionar_livro_a_pilha(genero, livro)
        elif opcao == "4":
            genero = input("Digite o nome do gênero: ")
            biblioteca.remover_livro_da_pilha(genero)
        elif opcao == "5":
            genero = input("Digite o nome do gênero: ")
            biblioteca.ver_topo_da_pilha(genero)
        elif opcao == "6":
            genero = input("Digite o nome do gênero: ")
            biblioteca.total_de_livros_na_pilha(genero)
        elif opcao == "7":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
