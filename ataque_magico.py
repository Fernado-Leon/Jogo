
from personagem import *
from CONFIG_JOGO import *
from Cronometro import *
import pygame as pg




class magia:
    def __init__(self):
        self.cronometro=cronometro()
        self.velocidade_magia=3
        self.x=ConfigJogo.LARGURA_TELA//4
        self.y=ConfigJogo.ALTURA_TELA//2
        self.posicao_magia=(self.x, self.y)
        self.termina=0
        
        
      
        
    def dano(self, tela:pg.Surface, jogador:Personagem, inimigo:Personagem):

           
            
            self.posicao_magia=(self.x, self.y)
            pg.draw.circle(
            surface=tela,
            color=(153, 255, 255),
            center=(self.posicao_magia),
            radius=85,
            width=0
            )
            if (((self.x-inimigo.posicao[0])**2)+ ((self.y-inimigo.posicao[1])**2))**0.5<=50:
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

    def tempo(self):
        if self.cronometro.tempo_passado()>5 or self.x>ConfigJogo.LARGURA_TELA or self.x<0 :
            self.termina=1
            self.cronometro.reset()
            
    def resetar_posicao(self, jogador):
        self.termina=0
        self.x=jogador.posicao[0]+ConfigJogo.meiotamanho_per
        self.y=jogador.posicao[1]+ConfigJogo.meiotamanho_per
        self.posicao_magia=(self.x, self.y)

              

        
           
           