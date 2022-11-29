import pygame as pg
from CONFIG_JOGO import ConfigJogo
import sys
from Cena_principal import *
from lista_personagens import stats




class Cenavitoria:
    def __init__(self, tela:pg.Surface, indice:int):
        self.tela =tela       
        self.fim= False
        self.indice=indice
        self.status=stats()
        

        # cria os textos que serao mostrados na tela
        font_titulo = pg.font.SysFont(None, ConfigJogo.FONTE_TITULO)
        self.titulo_1 = font_titulo.render(
            f'JOGADOR 1 VENCEU', True, (255,0,0))
        self.titulo_2 = font_titulo.render(
            f'JOGADOR 2 VENCEU', True, (20,0,255))
        self.titulo_3 = font_titulo.render(
            f'EMPATE', True, (128,128,128))
        

    def rodar(self):
        while not self.fim:
            self.tratamento_eventos()
            self.atualiza_estado()
            self.desenha()

    def tratamento_eventos(self):
   

        for event in pg.event.get():
            
            if (event.type == pg.QUIT) or \
                (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE) or \
                    (pg.key.get_pressed()[pg.K_ESCAPE]):
                self.status.reseta_tudo()
                self.fim = True
                ConfigJogo.Tela=1
          

    def atualiza_estado(self):
        pass

    def desenha(self):
        self.tela.fill((255, 255, 255))
        if self.indice==1:
            px = ConfigJogo.LARGURA_TELA // 2 - self.titulo_1.get_size()[0] // 2
            py = (ConfigJogo.ALTURA_TELA *.6)
            self.tela.blit(self.titulo_1, (px, py))
        if self.indice==2:
            px = ConfigJogo.LARGURA_TELA // 2 - self.titulo_2.get_size()[0] // 2
            py = (ConfigJogo.ALTURA_TELA *.6)
            self.tela.blit(self.titulo_2, (px, py))
        if self.indice==3:
            px = ConfigJogo.LARGURA_TELA // 2 - self.titulo_3.get_size()[0] // 2
            py = (ConfigJogo.ALTURA_TELA *.6)
            self.tela.blit(self.titulo_3, (px, py))
    
        
        



        pg.display.flip()