import f as ff
import os

os.system("cls")
while (True):
    
    a=int(input("Digite o primeiro valor:"))
    b=int(input("Digite o segundo valor:"))
    i=int(input("\n--------------------------------\n1.Soma\n2.Subtração\n3.Multiplicação\n4.Divisão\n5.Potenciação\n6.Radiacição\nDigite qual operaçao deseja fazer:\n----------------------------------\n"))

    def resultado(i):
        if i==1:
            resultado=ff.soma(a,b)
        elif i==2:
            resultado=ff.sub(a,b)
        elif i==3:
            resultado=ff.mult(a,b)
        elif i==4:
            resultado=ff.div(a,b)
        elif i==5:
            resultado=ff.pot(a,b)
        elif i==6:
            resultado=ff.rad(a,b)
    resultado(i)
