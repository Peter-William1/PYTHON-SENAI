class Pilha:
    def __init__(self):
        self.itens = []

    def empilhar(self, genero, livro, autor):
        self.itens.append((genero, livro, autor))

    def desempilhar(self):
        if self.vazia():
            return None
        return self.itens.pop()

    def vazia(self):
        return len(self.itens) == 0

def criar_pilha_com_nome(pilhas, nome):
    pilhas[nome] = Pilha()

def listar_pilhas(pilhas):
    print("Pilhas criadas:")
    for nome in pilhas:
        print(nome)
        conteudo = pilhas[nome].itens
        if len(conteudo) > 0:
            print("Conteúdo da pilha:")
            for genero, livro, autor in conteudo:
                print(f"Gênero: {genero}, Livro: {livro}, Autor: {autor}")

def quantos_livros(pilha):
    quantidade_livros = len(pilha.itens)
    return quantidade_livros

pilhas = {}

while True:
    print("\nOpções:")
    print("1) Adicionar um livro à pilha")
    print("2) Remover um livro do topo da pilha")
    print("3) Ver o topo da pilha")
    print("4) Mostrar o total de livros na pilha")
    print("5) Criar uma nova pilha")
    print("6) Listar pilhas criadas")
    print("7) Sair")

    op = int(input("Digite uma opção: "))

    if op == 1:
        nome_pilha = input("Digite o nome da pilha: ")
        genero = input("Digite o Gênero: ")
        livro = input("Digite o Nome do Livro: ")
        autor = input("Digite o Nome do Autor: ")
        
        if nome_pilha not in pilhas:
            criar_pilha_com_nome(pilhas, nome_pilha)
        
        pilha = pilhas[nome_pilha]
        pilha.empilhar(genero, livro, autor)
        print("Livro adicionado à pilha.")

    elif op == 2:
        nome_pilha = input("Digite o nome da pilha: ")
        
        if nome_pilha in pilhas:
            pilha = pilhas[nome_pilha]
            livro_removido = pilha.desempilhar()
            if livro_removido:
                genero, livro, autor = livro_removido
                print(f"Removido: Gênero: {genero}, Livro: {livro}, Autor: {autor}")
            else:
                print("A pilha está vazia.")
        else:
            print("Pilha não encontrada.")
    
    elif op == 3:
        nome_pilha = input("Digite o nome da pilha: ")
        if nome_pilha in pilhas:
            pilha = pilhas[nome_pilha]
            if not pilha.vazia():
                genero, livro, autor = pilha.itens[-1]
                print(f"Topo da pilha: Gênero: {genero}, Livro: {livro}, Autor: {autor}")
            else:
                print("A pilha está vazia.")
        else:
            print("Pilha não encontrada.")

    elif op == 4:
        nome_pilha = input("Digite o nome da pilha: ")
        if nome_pilha in pilhas:
            pilha = pilhas[nome_pilha]
            quantidade = quantos_livros(pilha)
            print(f"Total de livros na pilha: {quantidade}")
        else:
            print("Pilha não encontrada.")

    elif op == 5:
        nome_pilha = input("Digite o nome da nova pilha: ")
        criar_pilha_com_nome(pilhas, nome_pilha)
        print(f"Pilha '{nome_pilha}' criada.")

    elif op == 6:
        listar_pilhas(pilhas)

    elif op == 7:
        print("Saindo do programa.")
        break

    else:
        print("Opção inválida.")
