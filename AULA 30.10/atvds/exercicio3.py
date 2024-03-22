import os
os.system('cls')
class Livro:
    def __init__(self, titulo, autor, num_paginas, pagina_atual):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas
        self.pagina_atual = pagina_atual

    def avancar_pagina(self):
        if self.pagina_atual < self.num_paginas:
            self.pagina_atual +=1
        else: print("Você esta na ultima pagina!")
    def voltar_pagina(self):
        if self.pagina_atual >= 2:
            self.pagina_atual-=1
        else: print("Você esta na primeira pagina!")

    
livro = Livro("Senhor dos aneis", "Tolkien", 576, 1)

livro.avancar_pagina()
livro.voltar_pagina()
print(f"pagina atual:{livro.pagina_atual}")