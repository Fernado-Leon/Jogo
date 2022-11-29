import pygame, sys
from pygame.locals import *

ALTURA=400
LARGURA=400

POSICAO_X=0  
POSICAO_Y=0

TAM_X=100
TAM_Y=100

screen = pygame.display.set_mode((LARGURA, ALTURA))
sheet = pygame.image.load('/home/lcee/Área de Trabalho/miketyson.png')

sheet.set_clip(pygame.Rect(POSICAO_X, POSICAO_Y, TAM_X, TAM_Y))
draw_me = sheet.subsurface(sheet.get_clip())

backdrop = pygame.Rect(0, 0, LARGURA, ALTURA)

screen.blit(draw_me,backdrop)
pygame.display.flip()
