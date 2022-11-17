from personagem import *
from CONFIG_JOGO import *
from Cronometro import *
import pygame as pg
import math




class tirinho:
    def __init__(self):
        self.cronometro=cronometro()
        self.velocidade_magia_x=8
        self.velocidade_magia_y=8
        self.x=ConfigJogo.LARGURA_TELA//4
        self.y=ConfigJogo.ALTURA_TELA//2
        self.posicao_magia=(self.x, self.y)
        
        
      
        
    def dano(self, tela, jogador, inimigo):
           
          
            self.posicao_magia=(self.x, self.y)
            pg.draw.circle(
            surface=tela,
            color=(255, 50, 50),
            center=(self.posicao_magia),
            radius=10,
            width=0
            )
            if (self.x-inimigo.posicao[0])**2-(self.y-inimigo.posicao[1])**2<=50:
                inimigo.vida-=jogador.dano_magico//10
            self.mover_magia(jogador, inimigo)
           

    def mover_magia(self, jogador, inimigo):
            self.calcula_direcao(inimigo)

        
            self.x=self.x+self.velocidade_magia_x
            self.y+=self.velocidade_magia_y
            self.posicao_magia=(self.x, self.y)
            
    def resetar_posicao(self, jogador):
        self.x=jogador.posicao[0]+ConfigJogo.meiotamanho_per
        self.y=jogador.posicao[1]+ConfigJogo.meiotamanho_per
        self.posicao_magia=(self.x, self.y)
    def calcula_direcao(self, inimigo):
        tiro_vx = inimigo.posicao[0] - self.x
        tiro_vy = inimigo.posicao[1] - self.y
        
        norma = math.sqrt(tiro_vx ** 2 + tiro_vy ** 2)
        tiro_vx /= norma
        tiro_vy /= norma
          
        tiro_vx *= self.velocidade_magia_x
        tiro_vy *= self.velocidade_magia_y


              

        
           
           