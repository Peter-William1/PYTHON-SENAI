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
def main():
    pilhas = {}
    
    while True:
        print("Opções:")
        print("1. Criar nova pilha")
        print("2. Empilhar em uma pilha")
        
        
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            nome = input("Digite o nome da pilha: ")
            criar_pilha_com_nome(pilhas, nome)
            print(f"Pilha '{nome}' criada com sucesso!")
        elif opcao == "2":
            nome = input("Digite o nome da pilha: ")
            if nome in pilhas:
                valor = input("Digite o valor a ser empilhado: ")
                pilhas[nome].empilhar(valor)
                print(f"'{valor}' empilhado na pilha '{nome}'")
    
        break
            

if __name__ == "__main__":
    main()
