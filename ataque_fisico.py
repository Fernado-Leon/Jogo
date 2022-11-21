from personagem import *
from CONFIG_JOGO import *
from Cronometro import *
import pygame as pg
class fisico:
    def __init__(self):
        self.cronometro=cronometro()
        self.distancia_1=0
        self.distancia_2=0
        self.termina=0
      
        
    def dano(self, tela, jogador, inimigo):
            pg.draw.circle(
            surface=tela,
            color=(220, 0, 0),
            center=(jogador.posicao[0]+ConfigJogo.meiotamanho_per, jogador.posicao[1]+ConfigJogo.meiotamanho_per  ),
            radius=ConfigJogo.meiotamanho_per*2,
            width=5
            )
            self.distancia_1= ((jogador.posicao[0]+ConfigJogo.meiotamanho_per-inimigo.posicao[0])**2 +(jogador.posicao[1]+ConfigJogo.meiotamanho_per-inimigo.posicao[1])**2)**0.5
            self.distancia_2= ((inimigo.posicao[0]+ConfigJogo.meiotamanho_per-jogador.posicao[0])**2 +(inimigo.posicao[1]+ConfigJogo.meiotamanho_per-jogador.posicao[1])**2)**0.5
            if self.distancia_1<=50 or self.distancia_2<=50:
                inimigo.vida-=jogador.dano_fisico//10
    def tempo(self):
        if self.cronometro.tempo_passado()>1.75:
            self.termina=1
            self.cronometro.reset()
        return self.termina
    def reset(self):
        self.termina=0
    
            