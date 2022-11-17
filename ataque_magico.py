
from personagem import *
from CONFIG_JOGO import *
from Cronometro import *
import pygame as pg




class magia:
    def __init__(self):
        self.cronometro=cronometro()
        self.velocidade_magia=8
        self.x=ConfigJogo.LARGURA_TELA//4
        self.y=ConfigJogo.ALTURA_TELA//2
        self.posicao_magia=(self.x, self.y)
        
        
      
        
    def dano(self, tela, jogador, inimigo):
           
          
            self.posicao_magia=(self.x, self.y)
            pg.draw.circle(
            surface=tela,
            color=(153, 255, 255),
            center=(self.posicao_magia),
            radius=85,
            width=0
            )
            if (self.x-inimigo.posicao[0])**2-(self.y-inimigo.posicao[1])**2<=50:
                inimigo.vida-=jogador.dano_magico//10
            self.mover_magia(jogador)
           

    def mover_magia(self, jogador):
            if jogador.direcao==0:  
                if self.x<ConfigJogo.LARGURA_TELA:
                    self.x=self.x+self.velocidade_magia
                    self.posicao_magia=(self.x, self.y)
            if jogador.direcao==1:  
                if self.x<ConfigJogo.LARGURA_TELA:
                    self.x=self.x-self.velocidade_magia
                    self.posicao_magia=(self.x, self.y)
    def resetar_posicao(self, jogador):
        self.x=jogador.posicao[0]+ConfigJogo.meiotamanho_per
        self.y=jogador.posicao[1]+ConfigJogo.meiotamanho_per
        self.posicao_magia=(self.x, self.y)
              

        
           
           