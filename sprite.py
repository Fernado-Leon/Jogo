import pygame
from CONFIG_JOGO import ConfigJogo


tela = pygame.display.set_mode((ConfigJogo.LARGURA_TELA, ConfigJogo.ALTURA_TELA))
pygame.display.set_caption('Sprites')

sprite_sheet = pygame.image.load('spritesheet.png')

class Jogador(pygame.sprite.Sprite):
    def __init__(self, nome_jogador, pos_x, pos_y, direcao):
        pygame.sprite.Sprite.__init__(self)
        self.imagens_jogador = []
        self.nome_jogador = nome_jogador
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.direcao = direcao
        j = self.seleciona_personagem()
        
        # faz o recorte na spritesheet daas sprites de cada personagem
        for i in range(2):
            img  = sprite_sheet.subsurface((i*448, j*672), (448, 672))
            img = pygame.transform.scale(img, (45, 67))
            self.imagens_jogador.append(img)
        
        # desenha a primeira posicao do personagem 
        self.index_lista = 0 
        self.image = self.imagens_jogador[self.index_lista]
        self.rect = self.image.get_rect()
        # define a colisao dos personagens como uma mascara apenas dos pixels
        # podemos mudar esse tipo de colisao se tiver muito complicado
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y
    
    
    def seleciona_personagem(self):
        # seleciona o conjunto de sprite do personagem pelo nome
        lista_personagens = ['STALIN', 'GORBACHOV', 'IVAN DRAGO', 'RASPUTIN', 'RAMBO', 'MUHAMMAD ALI', 'JESSE JAMES', 'JOHN F KENNEDY']
        j = lista_personagens.index(self.nome_jogador)
        return j

    def update(self):
        '''NAO FUNCIONA'''
        # deveria selecionar a sprite correta dependendo da direcao
        if self.direcao == 0:
            self.index_lista = 0
        if self.direcao == 1:
            self.index_lista = 1
        self.image = self.imagens_jogador[self.index_lista]
        
       

