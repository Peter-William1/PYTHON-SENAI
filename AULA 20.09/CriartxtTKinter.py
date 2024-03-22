listaa = [
        
]

endereco= "arquivotexto.txt"

def list_nome(lista_final):
        nome_data=[a.pop(0)]
        
        lista_final.append(nome_data)
        


with open(endereco, "r") as arquivo:
        conteudo = arquivo.read()
        borococho = conteudo
        
        

a = borococho.split(" ")
print(a)
b = a[0].split("\n")
