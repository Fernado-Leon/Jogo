import pygame as pg
from CONFIG_JOGO import ConfigJogo
import sys



class Historia:
    def __init__(self, tela):
        self.tela = tela       
        self.fim= False

        # cria os textos que serao mostrados na tela
        font_titulo = pg.font.SysFont(None, ConfigJogo.FONTE_TITULO)
        font_subtitulo = pg.font.SysFont(None, ConfigJogo.Fonte_HISTORIA)
        self.titulo = font_subtitulo.render(
            f'Apos os eventos da tenebrosa guerra fria 1', True, ConfigJogo.COR_TITULO)
        self.subtitulo = font_subtitulo.render(
            f'o verão derreteu os planos de conquista mundial de URSS e USA', True, ConfigJogo.COR_TITULO)
        self.subtitulo2 = font_subtitulo.render(
            f'Porém após a segunda era glacial, a tecnologia', True, ConfigJogo.COR_TITULO)
        self.subtitulo3 = font_subtitulo.render(
            f'misteriosamente voltou a decada de 60 e a guerra esta de volta', True, ConfigJogo.COR_TITULO)
        self.subtitulo4 = font_subtitulo.render(
            f'Assim como a URSS', True, ConfigJogo.COR_TITULO)
        self.subtitulo5 = font_subtitulo.render(
            f'(Soyoz Nyerooshimiy Ryespooblik svobodnikh)', True, ConfigJogo.COR_TITULO)
        self.subtitulo6 = font_subtitulo.render(
            f'Os agentes precisam recuperar o santo Graal ', True, ConfigJogo.COR_TITULO)
        self.subtitulo7 = font_subtitulo.render(
            f'Com ele, poderão finalmente ressucitar...', True, ConfigJogo.COR_TITULO)
        self.subtitulo8= font_titulo.render(
            f'Napoleão, a cartada final', True, ConfigJogo.COR_TITULO)
        
        
        

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
                ConfigJogo.Tela=3
    def atualiza_estado(self):
        pass

    def desenha(self):
        self.tela.fill((255, 255, 255))
        px = ConfigJogo.LARGURA_TELA // 2 - self.titulo.get_size()[0] // 2
        py = (0.2 * ConfigJogo.ALTURA_TELA // 2)
        self.tela.blit(self.titulo, (px, py))
        px = ConfigJogo.LARGURA_TELA // 2 - \
        self.subtitulo.get_size()[0] // 2
        py = (0.2 * ConfigJogo.ALTURA_TELA // 2) + \
        (self.titulo.get_size()[1] * 1.5)
        self.tela.blit(self.subtitulo, (px, py))
        px = ConfigJogo.LARGURA_TELA // 2 - \
        self.subtitulo2.get_size()[0] // 2
        py = py+ (self.subtitulo.get_size()[1] * 1.5)
        self.tela.blit(self.subtitulo2, (px, py))
        px = ConfigJogo.LARGURA_TELA // 2 - \
        self.subtitulo3.get_size()[0] // 2
        py = py+ (self.subtitulo.get_size()[1] * 1.5)
        self.tela.blit(self.subtitulo3, (px, py))
        px = ConfigJogo.LARGURA_TELA // 2 - \
        self.subtitulo4.get_size()[0] // 2
        py = py+ (self.subtitulo.get_size()[1] * 1.5)
        self.tela.blit(self.subtitulo4, (px, py))
        px = ConfigJogo.LARGURA_TELA // 2 - \
        self.subtitulo5.get_size()[0] // 2
        py = py+ (self.subtitulo.get_size()[1] * 1.5)
        self.tela.blit(self.subtitulo5, (px, py))
        px = ConfigJogo.LARGURA_TELA // 2 - \
        self.subtitulo6.get_size()[0] // 2
        py = py+ (self.subtitulo.get_size()[1] * 1.5)
        self.tela.blit(self.subtitulo6, (px, py))
        px = ConfigJogo.LARGURA_TELA // 2 - \
        self.subtitulo7.get_size()[0] // 2
        py = py+ (self.subtitulo.get_size()[1] * 1.5)
        self.tela.blit(self.subtitulo7, (px, py))
        px = ConfigJogo.LARGURA_TELA // 2 - \
        self.subtitulo8.get_size()[0] // 2
        py = py+ (self.subtitulo.get_size()[1] * 1.5)
        self.tela.blit(self.subtitulo8, (px, py))
        
        pg.display.flip()



