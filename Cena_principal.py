
import sys
from typing import Tuple
import pygame as pg
from constantes import Constantes
from personagem import Personagem
from lista_personagens import *
from cena_selecao1 import *
from cena_selecao2 import *


class CenaPrincipal:
    def __init__(self, tela, per_1, per_2):
        self.tela = tela
        self.player_1=lista_1[per_1]
        self.player_2=lista_2[per_2]
        self.fim = False

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
                Constantes.Tela=1

       
            #if pg.key.get_pressed()[pg.K_SPACE]:
                #self.fim = True
                #ConfigJogo.Tela=4

        
            if pg.key.get_pressed()[pg.K_w]:
                self.player_1.mover_para_cima()
            elif pg.key.get_pressed()[pg.K_s]:
                self.player_1.mover_para_baixo()
            else:
                self.player_1.para_y()


            if pg.key.get_pressed()[pg.K_d]:
                self.player_1.mover_para_direita()
            elif pg.key.get_pressed()[pg.K_a]:
                self.player_1.mover_para_esquerda()
            else:
                self.player_1.para_x()

            if pg.key.get_pressed()[pg.K_i]:
                self.player_2.mover_para_cima()
            elif pg.key.get_pressed()[pg.K_k]:
                self.player_2.mover_para_baixo()
            else:
                self.player_2.para_y()
            if pg.key.get_pressed()[pg.K_l]:
                self.player_2.mover_para_direita()
            elif pg.key.get_pressed()[pg.K_j]:
                self.player_2.mover_para_esquerda()
            else:
                self.player_2.para_x()

    def atualiza_estado(self):
        self.player_1.atualizar_posicao()
        self.player_2.atualizar_posicao()
        

    def desenha(self):
        self.tela.fill((255, 255, 255))
        self.player_2.desenha(self.tela)
        self.player_1.desenha(self.tela)
        pg.display.flip()

   

   