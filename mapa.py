import pygame, sys
from  CONFIG_JOGO import ConfigJogo
from pytmx.util_pygame import load_pygame
from level import Level



pygame.init()
screen = pygame.display.set_mode(ConfigJogo.SIZE)
clock = pygame.time.Clock()
level = Level('gelo.tmx', screen)

while True:
    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')
    level.run()
    
    pygame.display.update()
    clock.tick(30)