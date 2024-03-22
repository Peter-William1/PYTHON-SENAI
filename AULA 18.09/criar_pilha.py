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


pilhas={}
nome="porragames"
criar_pilha_com_nome(pilhas,nome)
valor = input("")
pilhas[nome].empilhar(valor)
if nome in pilhas:
    listar_pilhas(pilhas)
pilhas[nome].pop()
if nome in pilhas:
    listar_pilhas(pilhas)