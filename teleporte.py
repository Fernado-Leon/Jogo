from personagem import *
from CONFIG_JOGO import *
from Cronometro import *
import pygame as pg




class dash:
    def __init__(self):
        self.cronometro=cronometro()
        self.termina=0
    def dano(self, tela:pg.Surface, jogador:Personagem, inimigo:Personagem, none):
        mouse_position = pg.mouse.get_pos()
        novo_x = mouse_position[0]
        novo_y = mouse_position[1]
        if ((novo_y >= 0) and \
                ((novo_y + ConfigJogo.tamanho_per) <= ConfigJogo.ALTURA_TELA)) and \
                    ((novo_x>=0) and ((novo_x +ConfigJogo.tamanho_per)<=ConfigJogo.LARGURA_TELA)):
            jogador.posicao=(novo_x, novo_y)


           
    def tempo(self):
        if self.cronometro.tempo_passado()>2.1:
            self.termina=1
            self.cronometro.reset()
            
    def resetar_posicao(self, jogador:Personagem):
       pass

              

        
           
           