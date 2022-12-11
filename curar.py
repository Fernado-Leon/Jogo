from personagem import *
from CONFIG_JOGO import *
from Cronometro import *
import pygame as pg




class cura:
    def __init__(self):
        self.cronometro=cronometro()
        self.termina=0
        
      
        
   
    def dano(self, tela:pg.Surface, jogador:Personagem, inimigo:Personagem, none):
        if self.cronometro.tempo_passado()>4:
            pg.draw.circle(
            surface=tela,
            color=(0, 220, 0),
            center=(jogador.posicao[0]+ConfigJogo.meiotamanho_per, jogador.posicao[1]+ConfigJogo.meiotamanho_per  ),
            radius=ConfigJogo.meiotamanho_per*2,
            
            )
            if jogador.vida<1000:
                jogador.vida+=jogador.dano_magico//100
    def tempo(self):
        if self.cronometro.tempo_passado()>4.5:
            self.termina=1
            self.cronometro.reset()
        return self.termina
    def reset(self):
        self.termina=0
    
        
        