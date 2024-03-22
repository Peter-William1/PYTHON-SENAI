import pygame
import random

# Inicialização do Pygame
pygame.init()

# Configurações da tela
largura, altura = 640, 480
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Pong")

# Cores
preto = (0, 0, 0)
branco = (255, 255, 255)

# Raquetes
raquete_largura, raquete_altura = 10, 100
raquete_jogador = pygame.Rect(50, altura // 2 - raquete_altura // 2, raquete_largura, raquete_altura)
raquete_oponente = pygame.Rect(largura - 50 - raquete_largura, altura // 2 - raquete_altura // 2, raquete_largura, raquete_altura)

# Bola
bola_tamanho = 10
bola = pygame.Rect(largura // 2 - bola_tamanho // 2, altura // 2 - bola_tamanho // 2, bola_tamanho, bola_tamanho)
bola_x_velocidade = 7 * random.choice((1, -1))
bola_y_velocidade = 7 * random.choice((1, -1))

# Pontuação
pontuacao_jogador = 0
pontuacao_oponente = 0
fonte = pygame.font.Font(None, 36)

def desenhar_elementos():
    tela.fill(preto)
    pygame.draw.rect(tela, branco, raquete_jogador)
    pygame.draw.rect(tela, branco, raquete_oponente)
    pygame.draw.ellipse(tela, branco, bola)
    pygame.draw.aaline(tela, branco, (largura // 2, 0), (largura // 2, altura))

def mover_raquetes():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and raquete_jogador.top > 0:
        raquete_jogador.y -= 10
    if keys[pygame.K_s] and raquete_jogador.bottom < altura:
        raquete_jogador.y += 10
    if keys[pygame.K_UP] and raquete_oponente.top > 0:
        raquete_oponente.y -= 10
    if keys[pygame.K_DOWN] and raquete_oponente.bottom < altura:
        raquete_oponente.y += 10

def mover_bola():
    global bola_x_velocidade, bola_y_velocidade, pontuacao_jogador, pontuacao_oponente

    bola.x += bola_x_velocidade
    bola.y += bola_y_velocidade

    if bola.top <= 0 or bola.bottom >= altura:
        bola_y_velocidade = -bola_y_velocidade

    if bola.colliderect(raquete_jogador) or bola.colliderect(raquete_oponente):
        bola_x_velocidade = -bola_x_velocidade

    if bola.left <= 0:
        pontuacao_oponente += 1
        reiniciar_jogo()
    elif bola.right >= largura:
        pontuacao_jogador += 1
        reiniciar_jogo()

def reiniciar_jogo():
    global bola_x_velocidade, bola_y_velocidade
    bola.x = largura // 2 - bola_tamanho // 2
    bola.y = altura // 2 - bola_tamanho // 2
    bola_x_velocidade *= random.choice((1, -1))
    bola_y_velocidade *= random.choice((1, -1))

def atualizar_pontuacao():
    texto = fonte.render(f"{pontuacao_jogador} - {pontuacao_oponente}", True, branco)
    tela.blit(texto, (largura // 2 - texto.get_width() // 2, 30))

# Loop principal do jogo
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    mover_raquetes()
    mover_bola()
    desenhar_elementos()
    atualizar_pontuacao()

    pygame.display.flip()

# Encerrar o Pygame
pygame.quit()
