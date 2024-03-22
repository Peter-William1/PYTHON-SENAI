#cria a pilha de livros
pilha_de_livros= []
lista_de_listas= [
    pilha_de_livros
]
class Pilha:
    def __init__(self):
        self.itens = []

    def empilhar(self, item):
        self.itens.append(item)
def criar_pilha():
    return Pilha()

def criar_pilha_com_nome(pilhas, nome):
    pilhas[nome] = Pilha()

def listar_pilhas(pilhas):
    print("Pilhas criadas:")
    for nome in pilhas:
        print(nome)
        conteudo = pilhas[nome].itens
        if len(conteudo) > 0:
            print("Conteúdo da pilha:")
            for item in conteudo:
                print(item)


def addlivros(pilha):
     genero=input("Digite o Genero:")
     livro=input("Qual Livro deseja adicionar a pilha:")
     autor=input("Qual autor deste livro:")
     pilha.append(genero)
     pilha.append(livro)
     pilha.append(autor)

def remover_livro(pilha):
     item_removido= pilha.pop()
     print(item_removido)

def quantos_livros(pilha):
     quantidade_livros= len(pilha)
     print(quantidade_livros)


pilhas= {}


op=int(input("Bem vindo!.\n1)Adicionar um livro a pilha.       2)Remover um livro do topo da pilha.          3)Ver o topo da pilha.      4)Mostrar o total de livros\nDigite uma opção:"))
if op==1:
     nome=input("Digite o nome do genero que deseja adicionar o livro")
     valor=input("digite o nome do livro")
     autor=input("digite o nome do autor")
     pilhas[nome].append(valor)
elif op==2:
     nome=input("Digite o nome do genero que deseja remover o livro")
elif op==3:
     print("Livro:", pilha_de_livros[0], "Autor:", pilha_de_livros[1])
elif op==4:
     quantos_livros(pilha_de_livros)
elif op ==5:
     nome=input("Digite o nome do genero")
     criar_pilha_com_nome(pilhas, nome)
 