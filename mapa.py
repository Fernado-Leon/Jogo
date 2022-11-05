import pygame
from constantes import Constantes

class Mapa:
    def __init__(self) -> None:
        pygame.init()
        size = [Constantes.LARGURA_TELA, Constantes.ALTURA_TELA]
        screen = pygame.display.set_mode(size)
        
        pygame.display.set_caption