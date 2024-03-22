import os
os.system('cls')

class Pessoa:
    def __init__(self, nome,email,idade):
        self.nome = nome
        if "@" in  email :
            self. email=email

        if idade > 0 : self.idade = idade
        else: self.idade =0

    def getNome(self): return self.nome
    def getEmail(self): return self.email
    def getIdade(self): return self.idade

    def setNome(self,novonome): self.nome = novonome
    def setEmail(self,novoemail): 
        if "@" and ".com" in  novoemail:
                self.email=novoemail
        else : self.email =  "email invalido"
    def setIdade(self,novoidade): 
        if novoidade > 0 : self.idade = novoidade
        else: self.idade =0
        


p1 = Pessoa('Peter', 'wpeterwil@gmail.com', 16)


print(f"primeiro nome:{p1.getNome()}")
print(f"primeiro email:{p1.getEmail()}")
print(f"primeira idade:{p1.getIdade()}")

p1.setNome('Carlos')
p1.setEmail('sample@mail.com')
p1.setIdade(22)

print(f"segundo nome:{p1.getNome()}")
print(f"segundo email:{p1.getEmail()}")
print(f"segunda idade:{p1.getIdade()}")
