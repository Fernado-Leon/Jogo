import pygame as pg
from CONFIG_JOGO import ConfigJogo
from lista_personagens import *
import sys



class CenaSelecao2:
    def __init__(self, tela:pg.Surface):
        self.tela = tela       
        self.fim= False
        self.indice=0
        self.lista=lista_2
        self.px=0
        self.py=0
        self.py_rect=(0.458 * ConfigJogo.ALTURA_TELA // 2) 
        


        # cria os textos que serao mostrados na tela
        font_titulo = pg.font.SysFont(None, ConfigJogo.FONTE_SUBTITULO)
        font_subtitulo = pg.font.SysFont(None, ConfigJogo.FONTE_SUBTITULO)
        self.titulo = font_titulo.render(
            f'JOGADOR 2', True, ConfigJogo.COR_TITULO)
        self.selecao1 = font_subtitulo.render(
            self.lista[0].nome, True, ConfigJogo.COR_TITULO)
        self.selecao2 = font_subtitulo.render(
            self.lista[1].nome, True, ConfigJogo.COR_TITULO)
        self.selecao3 = font_subtitulo.render(
           self.lista[2].nome, True, ConfigJogo.COR_TITULO)
        self.selecao4 = font_subtitulo.render(
            self.lista[3].nome, True, ConfigJogo.COR_TITULO)


    def rodar(self):
        while not self.fim:
            self.tratamento_eventos()
            self.atualiza_estado()
            self.desenha()

    def tratamento_eventos(self):
         for event in pg.event.get():
            
            if (event.type == pg.QUIT):
                sys.exit(0)
            if (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE) or \
                    (pg.key.get_pressed()[pg.K_ESCAPE]):
                self.fim = True
                ConfigJogo.Tela=1

       
            if pg.key.get_pressed()[pg.K_SPACE]:
                self.fim = True
                ConfigJogo.Tela=5
            if   (event.type == pg.KEYDOWN and event.key == pg.K_i) and self.indice>0:
                self.py_rect=self.py_rect-0.25* ConfigJogo.ALTURA_TELA // 2
                self.indice-=1
             
            if   (event.type == pg.KEYDOWN and event.key == pg.K_k) and self.indice<=2:
                self.py_rect=self.py_rect+0.25* ConfigJogo.ALTURA_TELA // 2
                self.indice+=1
              
                


    

        

    def atualiza_estado(self):
        pass

    def desenha(self):
        self.tela.fill((50, 100, 255))
        self.px = ConfigJogo.LARGURA_TELA // 2 - self.titulo.get_size()[0] // 2
        self.py = (0.2 * ConfigJogo.ALTURA_TELA // 2)
        self.tela.blit(self.titulo, (self.px, self.py))
        self.px = ConfigJogo.LARGURA_TELA // 2 - \
        self.selecao1.get_size()[0] // 2
        self.py = (0.5 * ConfigJogo.ALTURA_TELA // 2) 
        self.tela.blit(self.selecao1, (self.px, self.py))
        self.px = ConfigJogo.LARGURA_TELA // 2 - \
        self.selecao2.get_size()[0] // 2
        self.py = (0.75 * ConfigJogo.ALTURA_TELA // 2) 
        self.tela.blit(self.selecao2, (self.px, self.py))
        self.px = ConfigJogo.LARGURA_TELA // 2 - \
        self.selecao3.get_size()[0] // 2
        self.py = (1 * ConfigJogo.ALTURA_TELA // 2) 
        self.tela.blit(self.selecao3, (self.px, self.py))
        self.px = ConfigJogo.LARGURA_TELA // 2 - \
        self.selecao4.get_size()[0] // 2
        self.py = (1.25 * ConfigJogo.ALTURA_TELA // 2) 
        self.tela.blit(self.selecao4, (self.px, self.py))
        self.rect()
        pg.display.flip()
    def rect(self):
        pg.draw.rect(
            surface=self.tela,
            color=(255,255,255),
            rect=(self.px-0.02*ConfigJogo.LARGURA_TELA,self.py_rect,self.px+0.13*ConfigJogo.LARGURA_TELA
        // 2 , 0.1*ConfigJogo.ALTURA_TELA),
            width=3)
    def escolha(self)->int:
        return self.indice
