from personagem import Personagem
from CONFIG_JOGO import *
from Cronometro import *
import pygame as pg
class fisico:
    def __init__(self):
        self.cronometro=cronometro()
        self.distancia_1=0
        self.distancia_2=0
        self.termina=0
        self.velocidade_inicial=1
        self.inimigo=0
      
        
    def dano(self, tela:pg.Surface, jogador:Personagem, inimigo:Personagem, velocidade_inicial):
            self.inimigo=inimigo
            self.velocidade_inicial=velocidade_inicial
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
                inimigo.vida-=jogador.dano_fisico*3
                if jogador.posicao[0]<inimigo.posicao[0]:
                    novo_x = inimigo.posicao[0] + 50
                    if novo_x+ConfigJogo.tamanho_per<ConfigJogo.LARGURA_TELA:
                        inimigo.posicao = (novo_x, inimigo.posicao[1])
                        inimigo.velocidade_x_muda=0


                if jogador.posicao[0]>inimigo.posicao[0]:
                    novo_x = inimigo.posicao[0] - 50
                    if novo_x+ConfigJogo.tamanho_per>0:
                        inimigo.posicao = (novo_x, inimigo.posicao[1])
                        inimigo.velocidade_x_muda=0
                        inimigo.velocidade_y_muda=0


                   
    def tempo(self):
        if self.cronometro.tempo_passado()>3:
            self.inimigo.velocidade_x_muda=self.velocidade_inicial
            self.inimigo.velocidade_y_muda=self.velocidade_inicial
            self.termina=1
            self.cronometro.reset()
            
        return self.termina
    def reset(self):
        self.termina=0
        

    
            