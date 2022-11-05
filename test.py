import pygame
from pygame.locals import *


pygame.init()

tamanho_tela = (640, 480)
tela = pygame.display.set_mode(tamanho_tela)
tela.fill((255,255,255))

pygame.display.set_caption('Hello pygame')

tempo = pygame.time.Clock()

funcionando = True
while funcionando:
    tempo_corrido = tempo.tick(30)

    for evento in pygame.event.get():
        if evento.type == QUIT:
            funcionando = False
        if evento.type == KEYDOWN and evento.key == K_1:
            tela.fill((0,0,0))
        if pygame.mouse.get_pressed()[0]:
            tela.fill((255,0,0))

        # (x, y, largura,altura)
        r = pygame.draw.rect(tela,(0,0,0), (12, 20, 50, 100))
        pygame.draw.circle(tela, (0,0,0), (20, 50), 100)
        pygame.draw.line(tela, (0,255,0), (120, 20), (500, 100), 10)
        pygame.draw.lines(tela, (0,0,0), False, [(0,0), (100,100), (150,200), (70,50)])
        

        

        print(pygame.mouse.get_pos())
        

    pygame.display.update()
