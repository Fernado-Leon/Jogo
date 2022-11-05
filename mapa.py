import pygame
from constantes import ConfigJogo

class Mapa:
    def __init__(self) -> None:
        pygame.init()
        size = [ConfigJogo.LARGURA_TELA, ConfigJogo.ALTURA_TELA]
        screen = pygame.display.set_mode(size)
        
        pygame.display.set_caption