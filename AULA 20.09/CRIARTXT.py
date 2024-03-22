loop=False
while loop==False:
    #Nome 
    nome=input("Digite seu nome:")
    #Data
    data=input("Escreve a data")

    #arquivo
    nome_arquivo ="arquivotexto.txt"


    #abre o arquivo no modo escrita
    with open(nome_arquivo, "a") as arquivo:
        arquivo.write(nome+" "+data+"\n")
    
    

    op= input("deseja continuar?\n1)Sim   2)Não\n")
    if op== "1":
        loop=False
    elif op=="2":
        print("encerrando sistema...")
        loop=True
