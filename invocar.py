from personagem import *
from CONFIG_JOGO import *
from Cronometro import *
import pygame as pg
import math
import random
from random import randint
from typing import List

class minion:
    def __init__(self, soldado:List[Personagem]):
        self.cronometro=cronometro()
        self.distancia_1=0
        self.distancia_2=0
        self.soldado=soldado
        self.x_1 = randint(0, 1280)
        self.y_1 = randint(0, 640) 
        self.x_2 = randint(0, 1280)
        self.y_2 = randint(0, 640) 
        self.x_3 = randint(0, 1280)
        self.y_3 = randint(0, 640) 
        self.l = ConfigJogo.meiotamanho_per
        self.a = ConfigJogo.meiotamanho_per
        self.posicao_minion_1=(self.x_1, self.y_1, self.l, self.a)
        self.posicao_minion_2=(self.x_2, self.y_2, self.l, self.a)
        self.posicao_minion_3=(self.x_3, self.y_3, self.l, self.a)
        self.tela=0
        self.termina=1
        self.aleatorio=random.randint(1, 4)
        self.desenhado_1=0
        self.desenhado_2=0

      
        
    def dano(self, tela:pg.Surface, jogador:Personagem, inimigo:Personagem, none):
            self.tela=tela
            self.desenha(self.tela) 
            if(((self.x_1-inimigo.posicao[0])**2)+ ((self.y_1-inimigo.posicao[1])**2))**0.5<=50 and self.desenhado_1==1:
                inimigo.vida-=self.soldado[1].dano_fisico//20
               
            if (((self.x_2-inimigo.posicao[0])**2)+ ((self.y_2-inimigo.posicao[1])**2))**0.5<=50  and self.desenhado_2==1:
                inimigo.vida-=self.soldado[1].dano_fisico//20
            self.mover_minion_1(inimigo)
            self.mover_minion_2(inimigo)
            self.mover_minion_3(inimigo)
    def desenha(self, tela:pg.Surface):
          
            self.posicao_minion_1=(self.x_1, self.y_1, self.l, self.a)
            self.posicao_minion_2=(self.x_2, self.y_2, self.l, self.a)
       
            if self.aleatorio>=1:
                pg.draw.rect(
                tela,
                (0,0,0),
                pg.rect.Rect((self.posicao_minion_1))
                   )
                self.desenhado_1=1
                if self.aleatorio>=2:
                    pg.draw.rect(
                    tela,
                    (0,0,0),
                    pg.rect.Rect((self.posicao_minion_2))
                     )
                    self.desenhado_2=1
                    if self.aleatorio>=3:
                        pg.draw.rect(
                        tela,
                        (0,0,0),
                        pg.rect.Rect((self.posicao_minion_3))
                        )
                        self.desenhado_2=1
    def mover_minion_1(self, inimigo:Personagem):
        dist_1 = math.sqrt(
        (inimigo.posicao[0] - self.x_1) ** 2 +
        (inimigo.posicao[1] - self.y_1) ** 2
        )

        if dist_1 > ConfigJogo.meiotamanho_per:
        
            minion_vx_1 = inimigo.posicao[0] - self.x_1
            minion_vy_1 = inimigo.posicao[1] - self.y_1
        
            norma = math.sqrt(minion_vx_1 ** 2 + minion_vy_1 ** 2)
            minion_vx_1 /= norma
            minion_vy_1 /= norma
          
            minion_vx_1 *= 5*(self.soldado[2].velocidade)
            minion_vy_1 *= 5*(self.soldado[2].velocidade)
        else:
            minion_vx_1 = 0
            minion_vy_1 = 0

        if not ((self.y_1<128 and self.y_1>64-ConfigJogo.meiotamanho_per)  and (self.x_1>128-ConfigJogo.meiotamanho_per and self.x_1<224)):
                if not ((self.y_1<128 and self.y_1>64-ConfigJogo.meiotamanho_per)  and (self.x_1>1056-ConfigJogo.meiotamanho_per and self.x_1<1152)):
                    if not ((self.y_1<576 and self.y_1>512-ConfigJogo.meiotamanho_per)  and (self.x_1>128-ConfigJogo.meiotamanho_per and self.x_1<224)):
                        if not ((self.y_1<576 and self.y_1>512-ConfigJogo.meiotamanho_per)  and (self.x_1>1056-ConfigJogo.meiotamanho_per and self.x_1<1152)):
                            if not ((self.y_1<576 and self.y_1>448-ConfigJogo.meiotamanho_per)  and (self.x_1>448-ConfigJogo.meiotamanho_per and self.x_1<480)):
                                if not ((self.y_1<576 and self.y_1>448-ConfigJogo.meiotamanho_per)  and (self.x_1>800-ConfigJogo.meiotamanho_per and self.x_1<832)):
                                    if not ((self.y_1<192 and self.y_1>64-ConfigJogo.meiotamanho_per)  and (self.x_1>448-ConfigJogo.meiotamanho_per and self.x_1<480)):
                                        if not ((self.y_1<192 and self.y_1>64-ConfigJogo.meiotamanho_per)  and (self.x_1>800-ConfigJogo.meiotamanho_per and self.x_1<832)):    
                                            self.x_1 += minion_vx_1
                                            self.y_1 += minion_vy_1
        self.posicao_minion_1=(self.x_1, self.y_1, self.l, self.a)
    def mover_minion_2(self, inimigo:Personagem):
        dist_2 = math.sqrt(
        (inimigo.posicao[0] - self.x_2) ** 2 +
        (inimigo.posicao[1] - self.y_2) ** 2
        )

        if dist_2 > ConfigJogo.meiotamanho_per:
        
            minion_vx_2 = inimigo.posicao[0] - self.x_2
            minion_vy_2 = inimigo.posicao[1] - self.y_2
        
            norma = math.sqrt(minion_vx_2 ** 2 + minion_vy_2 ** 2)
            minion_vx_2 /= norma
            minion_vy_2 /= norma
          
            minion_vx_2 *= 5*(self.soldado[2].velocidade)
            minion_vy_2 *= 5*(self.soldado[2].velocidade)
        else:
            minion_vx_2 = 0
            minion_vy_2 = 0

    
        
        if not ((self.y_2<128 and self.y_2>64-ConfigJogo.meiotamanho_per)  and (self.x_2>128-ConfigJogo.meiotamanho_per and self.x_2<224)):
                if not ((self.y_2<128 and self.y_2>64-ConfigJogo.meiotamanho_per)  and (self.x_2>1056-ConfigJogo.meiotamanho_per and self.x_2<1152)):
                    if not ((self.y_2<576 and self.y_2>512-ConfigJogo.meiotamanho_per)  and (self.x_2>128-ConfigJogo.meiotamanho_per and self.x_2<224)):
                        if not ((self.y_2<576 and self.y_2>512-ConfigJogo.meiotamanho_per)  and (self.x_2>1056-ConfigJogo.meiotamanho_per and self.x_2<1152)):
                            if not ((self.y_2<576 and self.y_2>448-ConfigJogo.meiotamanho_per)  and (self.x_2>448-ConfigJogo.meiotamanho_per and self.x_2<480)):
                                if not ((self.y_2<576 and self.y_2>448-ConfigJogo.meiotamanho_per)  and (self.x_2>800-ConfigJogo.meiotamanho_per and self.x_2<832)):
                                    if not ((self.y_2<192 and self.y_2>64-ConfigJogo.meiotamanho_per)  and (self.x_2>448-ConfigJogo.meiotamanho_per and self.x_2<480)):
                                        if not ((self.y_2<192 and self.y_2>64-ConfigJogo.meiotamanho_per)  and (self.x_2>800-ConfigJogo.meiotamanho_per and self.x_2<832)):
                                            self.x_2 += minion_vx_2
                                            self.y_2 += minion_vy_2
        self.posicao_minion_2=(self.x_2, self.y_2, self.l, self.a)
    def mover_minion_3(self, inimigo:Personagem):
        dist_3 = math.sqrt(
        (inimigo.posicao[0] - self.x_3) ** 2 +
        (inimigo.posicao[1] - self.y_3) ** 2
        )

        if dist_3 > ConfigJogo.meiotamanho_per:
        
            minion_vx_3 = inimigo.posicao[0] - self.x_3
            minion_vy_3 = inimigo.posicao[1] - self.y_3
        
            norma = math.sqrt(minion_vx_3 ** 2 + minion_vy_3 ** 2)
            minion_vx_3 /= norma
            minion_vy_3 /= norma
          
            minion_vx_3 *= 5*(self.soldado[2].velocidade)
            minion_vy_3 *= 5*(self.soldado[2].velocidade)
        else:
            minion_vx_3 = 0
            minion_vy_3 = 0

    
        if not ((self.y_3<128 and self.y_3>64-ConfigJogo.meiotamanho_per)  and (self.x_3>128-ConfigJogo.meiotamanho_per and self.x_3<224)):
                if not ((self.y_3<128 and self.y_3>64-ConfigJogo.meiotamanho_per)  and (self.x_3>1056-ConfigJogo.meiotamanho_per and self.x_3<1152)):
                    if not ((self.y_3<576 and self.y_3>512-ConfigJogo.meiotamanho_per)  and (self.x_3>128-ConfigJogo.meiotamanho_per and self.x_3<224)):
                        if not ((self.y_3<576 and self.y_3>512-ConfigJogo.meiotamanho_per)  and (self.x_3>1056-ConfigJogo.meiotamanho_per and self.x_3<1152)):
                            if not ((self.y_3<576 and self.y_3>448-ConfigJogo.meiotamanho_per)  and (self.x_3>448-ConfigJogo.meiotamanho_per and self.x_3<480)):
                                if not ((self.y_3<576 and self.y_3>448-ConfigJogo.meiotamanho_per)  and (self.x_3>800-ConfigJogo.meiotamanho_per and self.x_3<832)):
                                    if not ((self.y_3<192 and self.y_3>64-ConfigJogo.meiotamanho_per)  and (self.x_3>448-ConfigJogo.meiotamanho_per and self.x_3<480)):
                                        if not ((self.y_3<192 and self.y_3>64-ConfigJogo.meiotamanho_per)  and (self.x_3>800-ConfigJogo.meiotamanho_per and self.x_3<832)):
                                            self.x_3 += minion_vx_3
                                            self.y_3 += minion_vy_3
        self.posicao_minion_3=(self.x_3, self.y_3, self.l, self.a)
    def tempo(self):
        if self.cronometro.tempo_passado()>6:
            self.termina= 1
            self.cronometro.reset()
        return self.termina
    def reset(self):
        self.aleatorio=random.randint(1, 4)
        self.termina=0
        self.x_1 = randint(0, 1280)
        self.y_1 = randint(0, 640) 
        self.x_2 = randint(0, 1280)
        self.y_2 = randint(0, 640) 
        self.x_3 = randint(0, 1280)
        self.y_3 = randint(0, 640) 
        self.desenhado_1==0
        self.desenhado_2==0
        
    
        