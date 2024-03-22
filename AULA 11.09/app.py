#Declarando e inicialização de uma lista com 3 elementos
cidades = ["Juiz de Fora","Matias Barbosa","Bom Jardim de Minas", "Piau", "Belo Horizonte"]

#Declarando uma lista vazia
cidades2=[]

#imprimindo a lista
print(cidades)

#imprimindo o segundo item da lista
print(cidades[1])

#imprimindo o ultimo item da lista
print(cidades[-1])

#mostra os 3 primeiros
print(cidades[:3])

#mostra os demais valores a pos  3
print(cidades[3:])

#mostra o intervalo
print(cidades[2:6])

#exibindo itens da linha 
for i in range(0,len(cidades)):
    print(cidades[i])

#exibindo itens da linha 
for a in cidades: print(a)

#incluir elemento
cidades.append("Uba")
cidades.insert(1, "Rio de Janeiro")
cidades.insert(0, "Uberlandia")
cidades.append(-0, "Rio Novo")

#Remover um elemento
cidades.remove("Rio de Janeiro")
cidades.pop(3)

#limpar lista
cidades.clear()