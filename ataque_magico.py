
from personagem import *
from CONFIG_JOGO import *
from Cronometro import *
from level import *
import pygame as pg




class magia:
    def __init__(self):
        self.cronometro=cronometro()
        self.velocidade_magia=3
        self.x=ConfigJogo.LARGURA_TELA//4
        self.y=ConfigJogo.ALTURA_TELA//2
        self.posicao_magia=(self.x, self.y)
        self.termina=0
        self.mapa=" "
        
        
      
        
    def dano(self, tela:pg.Surface, jogador:Personagem, inimigo:Personagem, level:Level):
            self.mapa=level
            self.posicao_magia=(self.x, self.y)
            pg.draw.circle(
            surface=tela,
            color=(153, 255, 255),
            center=(self.posicao_magia),
            radius=85,
            width=0
            )
            if (((self.x-inimigo.posicao[0])**2)+ ((self.y-inimigo.posicao[1])**2))**0.5<=85:
                inimigo.vida-=jogador.dano_magico//10
            self.quebrar()
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
        if self.cronometro.tempo_passado()>5 or self.x>=ConfigJogo.LARGURA_TELA or self.x<=0 :
            self.termina=1
            self.cronometro.reset()
            
    def resetar_posicao(self, jogador):
        self.termina=0
        self.x=jogador.posicao[0]+ConfigJogo.meiotamanho_per
        self.y=jogador.posicao[1]+ConfigJogo.meiotamanho_per
        self.posicao_magia=(self.x, self.y)
    def quebrar(self):
        if  ((self.y<576 and self.y>448-ConfigJogo.tamanho_per)  and (self.x>448-ConfigJogo.tamanho_per and self.x<480)):
            self.mapa.muda_mapa(1)
            print("1")
        if  ((self.y<576 and self.y>448-ConfigJogo.tamanho_per)  and (self.x>800-ConfigJogo.tamanho_per and self.x<832)):
            self.mapa.muda_mapa(2)
            print("2")
        if ((self.y<192 and self.y>64-ConfigJogo.tamanho_per)  and (self.x>448-ConfigJogo.tamanho_per and self.x<480)):
            self.mapa.muda_mapa(3)
            print("3")
        if ((self.y<192 and self.y>64-ConfigJogo.tamanho_per)  and (self.x>800-ConfigJogo.tamanho_per and self.x<832)):
            self.mapa.muda_mapa(4)
            print("4")
                        

              

        
           
           