
import pygame as pg
from constantes import ConfigJogo
import sys



class Cenainicial:
    def __init__(self, tela):
        self.tela = tela       
        self.fim= False

        # cria os textos que serao mostrados na tela
        font_titulo = pg.font.SysFont(None, ConfigJogo.FONTE_TITULO)
        font_subtitulo = pg.font.SysFont(None, ConfigJogo.FONTE_SUBTITULO)
        self.titulo = font_titulo.render(
            f'GUERRA FRIA 2', True, ConfigJogo.COR_TITULO)
        self.subtitulo = font_subtitulo.render(
            f'POR LUCA, FERNANDO E BERNARDO', True, ConfigJogo.COR_TITULO)

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
        
                sys.exit(0)

       
            if pg.key.get_pressed()[pg.K_SPACE]:
                self.fim = True
                ConfigJogo.Tela=2

    def atualiza_estado(self):
        pass

    def desenha(self):
        self.tela.fill((255, 255, 255))
        px = ConfigJogo.LARGURA_TELA // 2 - self.titulo.get_size()[0] // 2
        py = (0.3 * ConfigJogo.ALTURA_TELA // 2)
        self.tela.blit(self.titulo, (px, py))
        px = ConfigJogo.LARGURA_TELA // 2 - \
        self.subtitulo.get_size()[0] // 2
        py = (0.3 * ConfigJogo.ALTURA_TELA // 2) + \
        (self.titulo.get_size()[1] * 1.5)
        self.tela.blit(self.subtitulo, (px, py))





        pg.display.flip()



