
import sys
from typing import Tuple
import pygame as pg
from CONFIG_JOGO import ConfigJogo
from personagem import Personagem
from lista_personagens import *
from Cena_Selecao1 import *
from Cena_Selecao2 import *
from Cronometro import *
from ataque_fisico import *


class CenaPrincipal:
    def __init__(self, tela, per_1, per_2):
        self.indice_1=per_1
        self.indice_2=per_2
        self.tela = tela
        self.player_1=lista_1[per_1]
        self.player_2=lista_2[per_2]
        self.fim = False
        self.cronometro_1=cronometro()
        self.cronometro_2=cronometro()
        self.cronometro_ataque_1=cronometro()
        self.cronometro_ataque_2=cronometro()
        self.vida_1=self.player_1.vida
        self.vida_2=self.player_2.vida
    def rodar(self):
        while not self.fim:
            self.desenha()
            self.tratamento_eventos()
            self.atualiza_estado()

    def tratamento_eventos(self):
        for event in pg.event.get():
            
            if (event.type == pg.QUIT):
                sys.exit(0)
            if (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE) or \
                    (pg.key.get_pressed()[pg.K_ESCAPE]) or \
                        (self.player_1.vida<0 or self.player_2.vida<0):
                self.fim = True
                ConfigJogo.Tela=1
                self.player_1.vida=self.vida_1
                self.player_2.vida=self.vida_2
                

       
            #if pg.key.get_pressed()[pg.K_SPACE]:
                #self.fim = True
                #ConfigJogo.Tela=4

        
            if pg.key.get_pressed()[pg.K_w] :
                self.player_1.mover_para_cima()
            elif pg.key.get_pressed()[pg.K_s]:
                self.player_1.mover_para_baixo()
            else:
                self.player_1.para_y()


            if pg.key.get_pressed()[pg.K_d]:
                self.player_1.mover_para_direita()
            elif pg.key.get_pressed()[pg.K_a]:
                self.player_1.mover_para_esquerda()
            else:
                self.player_1.para_x()

            if pg.key.get_pressed()[pg.K_i]   :
                self.player_2.mover_para_cima()
            elif pg.key.get_pressed()[pg.K_k]:
                self.player_2.mover_para_baixo()
            else:
                self.player_2.para_y()
            if pg.key.get_pressed()[pg.K_l]:
                self.player_2.mover_para_direita()
            elif pg.key.get_pressed()[pg.K_j]:
                self.player_2.mover_para_esquerda()
                
                
            else:
                self.player_2.para_x()
           
        


    def atualiza_estado(self):
        self.player_1.atualizar_posicao()
        self.player_2.atualizar_posicao()
        
      
        

    def desenha(self):

        self.tela.fill((255, 255, 255))
      
        self.ataca_player_1()
        self.ataca_player_2()
        self.player_2.desenha(self.tela)
        self.player_1.desenha(self.tela)
        
               
        pg.display.flip()
    def ataca_player_1(self):
                
            if  pg.key.get_pressed()[pg.K_z] and self.cronometro_1.tempo_passado()>2   :
                    self.player_1.ataque[1].dano(self.tela, self.player_1, self.player_2)
                    if self.cronometro_1.tempo_passado()>2.8:
                        self.player_1.ataque[1].resetar_posicao(self.player_1)
                        self.cronometro_1.reset()
                
            if  pg.key.get_pressed()[pg.K_q] and self.cronometro_ataque_1.tempo_passado()>1.5 :
                    self.player_1.ataque[0].dano(self.tela, self.player_1, self.player_2)
                    self.player_1.ataque[0].tempo()
                    if self.player_1.ataque[0].termina==1:
                        self.cronometro_ataque_1.reset() 
                        self.player_1.ataque[0].reset() 
    def ataca_player_2(self):   
                
            if  pg.key.get_pressed()[pg.K_o] and self.cronometro_ataque_2.tempo_passado()>1.5 :
                    self.player_2.ataque[0].dano(self.tela, self.player_2, self.player_1)
                    self.player_2.ataque[0].tempo()
                    if self.player_2.ataque[0].termina==1:
                        self.cronometro_ataque_2.reset()
                        self.player_2.ataque[0].reset()



            if  pg.key.get_pressed()[pg.K_p] and self.cronometro_2.tempo_passado()>2  :
                    self.player_2.ataque[1].dano(self.tela, self.player_2, self.player_1)
                    if self.cronometro_2.tempo_passado()>2.8:
                        self.player_2.ataque[1].resetar_posicao(self.player_2)
                        self.cronometro_2.reset()       
          


   

   