import pygame
import sys

# Inicialize o Pygame
pygame.init()

# Defina as dimensões da janela
largura_janela = 800
altura_janela = 600

# Defina as cores
cor_fundo = (255, 255, 255)
cor_circulo = (0, 0, 255)
cor_retangulo = (255, 0, 0)

# Crie a janela
janela = pygame.display.set_mode((largura_janela, altura_janela))
pygame.display.set_caption("Animação de Círculo para Retângulo")

# Variáveis para controlar a forma atual
forma_circulo = True

# Variáveis para controlar as dimensões do retângulo
largura_retangulo = 0
altura_retangulo = 0

# Posição do centro do círculo
x_circulo = largura_janela // 2
y_circulo = altura_janela // 2

# Taxa de aumento das dimensões do retângulo (velocidade da animação)
taxa_aumento = 1

# Loop principal do jogo
rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if forma_circulo:
                forma_circulo = False
            else:
                forma_circulo = True

    # Preencher a tela com a cor de fundo
    janela.fill(cor_fundo)

    if forma_circulo:
        # Desenhar um círculo
        pygame.draw.circle(janela, cor_circulo, (x_circulo, y_circulo), 50)
    else:
        # Aumentar gradualmente as dimensões do retângulo para criar uma animação suave
        if largura_retangulo < 200:
            largura_retangulo += taxa_aumento
            altura_retangulo += taxa_aumento
        # Desenhar um retângulo com as dimensões animadas
        pygame.draw.rect(janela, cor_retangulo, (x_circulo - largura_retangulo // 2, y_circulo - altura_retangulo // 2, largura_retangulo, altura_retangulo), border_radius=11)

    # Atualizar a tela
    pygame.display.flip()
    

# Encerrar o Pygame
pygame.quit()
sys.exit()
