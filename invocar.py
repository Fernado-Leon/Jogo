from personagem import *
from CONFIG_JOGO import *
from Cronometro import *
import pygame as pg
import math

class minion:
    def __init__(self, soldado_1, soldado_2):
        self.cronometro=cronometro()
        self.distancia_1=0
        self.distancia_2=0
        self.soldado_1=soldado_1
        self.soldado_2=soldado_2
        self.x_1=self.soldado_1.posicao[0]
        self.y_1=self.soldado_1.posicao[1]
        self.x_2=self.soldado_2.posicao[0]
        self.y_2=self.soldado_2.posicao[1]
        self.l = ConfigJogo.meiotamanho_per
        self.a = ConfigJogo.meiotamanho_per
        self.posicao_minion_1=(self.x_1, self.y_1, self.l, self.a)
        self.posicao_minion_2=(self.x_2, self.y_2, self.l, self.a)
        self.tela=0
        self.termina=1

      
        
    def dano(self, tela, jogador, inimigo):
            self.tela=tela
            self.desenha(self.tela)
            
            self.distancia_1a= ((self.x_1+ConfigJogo.meiotamanho_per//2-inimigo.posicao[0])**2 +(self.y_1+ConfigJogo.meiotamanho_per//2-inimigo.posicao[1])**2)**0.5
            self.distancia_1b= ((inimigo.posicao[0]+ConfigJogo.meiotamanho_per-self.x_1)**2 +(inimigo.posicao[1]+ConfigJogo.meiotamanho_per-self.y_1)**2)**0.5
            self.distancia_2a= ((self.x_2+ConfigJogo.meiotamanho_per//2-inimigo.posicao[0])**2 +(self.y_2+ConfigJogo.meiotamanho_per//2-inimigo.posicao[1])**2)**0.5
            self.distancia_2b= ((inimigo.posicao[0]+ConfigJogo.meiotamanho_per-self.x_2)**2 +(inimigo.posicao[1]+ConfigJogo.meiotamanho_per-self.y_2)**2)**0.5
         
            if self.distancia_1a<=50 or self.distancia_1a<=50:
                inimigo.vida-=self.soldado_1.dano_fisico//20
            if self.distancia_2a<=50 or self.distancia_2a<=50:
                inimigo.vida-=self.soldado_2.dano_fisico//20
            self.mover_minion_1(inimigo)
            self.mover_minion_2(inimigo)
    def desenha(self, tela):
            self.posicao_minion_1=(self.x_1, self.y_1, self.l, self.a)
            self.posicao_minion_2=(self.x_2, self.y_2, self.l, self.a)
       
           
            pg.draw.rect(
            tela,
            (0,0,0),
            pg.rect.Rect((self.posicao_minion_1))
        )
            pg.draw.rect(
            tela,
            (0,0,0),
            pg.rect.Rect((self.posicao_minion_2))
        )
    def mover_minion_1(self, inimigo):
        dist_1 = math.sqrt(
        (inimigo.posicao[0] - self.x_1) ** 2 +
        (inimigo.posicao[1] - self.y_1) ** 2
        )

        if dist_1 > ConfigJogo.tamanho_per:
        
            minion_vx_1 = inimigo.posicao[0] - self.x_1
            minion_vy_1 = inimigo.posicao[1] - self.y_1
        
            norma = math.sqrt(minion_vx_1 ** 2 + minion_vy_1 ** 2)
            minion_vx_1 /= norma
            minion_vy_1 /= norma
          
            minion_vx_1 *= self.soldado_1.velocidade
            minion_vy_1 *= self.soldado_1.velocidade
        else:
            minion_vx_1 = 0
            minion_vy_1 = 0

    
        self.x_1 += minion_vx_1
        self.y_1 += minion_vy_1
        self.posicao_minion_1=(self.x_1, self.y_1, self.l, self.a)
    def mover_minion_2(self, inimigo):
        dist_2 = math.sqrt(
        (inimigo.posicao[0] - self.x_2) ** 2 +
        (inimigo.posicao[1] - self.y_2) ** 2
        )

        if dist_2 > ConfigJogo.tamanho_per:
        
            minion_vx_2 = inimigo.posicao[0] - self.x_2
            minion_vy_2 = inimigo.posicao[1] - self.y_2
        
            norma = math.sqrt(minion_vx_2 ** 2 + minion_vy_2 ** 2)
            minion_vx_2 /= norma
            minion_vy_2 /= norma
          
            minion_vx_2 *= self.soldado_2.velocidade
            minion_vy_2 *= self.soldado_2.velocidade
        else:
            minion_vx_2 = 0
            minion_vy_2 = 0

    
        self.x_2 += minion_vx_2
        self.y_2 += minion_vy_2
        self.posicao_minion_2=(self.x_2, self.y_2, self.l, self.a)
    def tempo(self):
        if self.cronometro.tempo_passado()>4:
            self.termina= 1
            self.cronometro.reset()
        return self.termina
    def reset(self):
        self.termina=0
        self.x_1=ConfigJogo.LARGURA_TELA//2
        self.y_1=ConfigJogo.ALTURA_TELA*.75
        self.x_2=ConfigJogo.LARGURA_TELA//2
        self.y_2=ConfigJogo.ALTURA_TELA//4
        
    
        