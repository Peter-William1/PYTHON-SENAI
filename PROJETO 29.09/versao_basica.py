import pygame
import sys



#inicia o app
pygame.init()

#Tela
altura= 500
largura= 500
tela= pygame.display.set_mode((largura, altura))
imagem_fundo = pygame.image.load("img_bg.png")
imagem_fundo = pygame.transform.scale(imagem_fundo, (altura, largura))
posicao_fundo = imagem_fundo.get_rect()



#loop do app
loop= True
while loop== True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        


    tela.blit(imagem_fundo, posicao_fundo)
    pygame.display.update()