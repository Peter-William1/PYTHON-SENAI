import pygame
import sys

pygame.init()

# Configurações da tela
largura = 400
altura = 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Aplicativo de Notas')

# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)

# Fonte e tamanho
fonte = pygame.font.Font(None, 24)

# Largura máxima da caixa de texto
largura_caixa_texto = 300

texto_digitado = ""

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RETURN:
                texto_digitado += "\n"
            elif evento.key == pygame.K_BACKSPACE:
                texto_digitado = texto_digitado[:-1]
            else:
                texto_digitado += evento.unicode

    tela.fill(branco)

    # Quebra o texto em linhas com base na largura máxima
    linhas = []
    linha_atual = ""
    for palavra in texto_digitado.split():
        teste = linha_atual + " " + palavra if linha_atual else palavra
        largura_texto, _ = fonte.size(teste)
        if largura_texto <= largura_caixa_texto:
            linha_atual = teste
        else:
            linhas.append(linha_atual)
            linha_atual = palavra
    if linha_atual:
        linhas.append(linha_atual)

    y = 50

    for linha in linhas:
        texto_renderizado = fonte.render(linha, True, preto)
        tela.blit(texto_renderizado, (20, y))
        y += texto_renderizado.get_height()

    pygame.display.flip()
