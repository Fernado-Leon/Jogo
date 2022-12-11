
import sys
from typing import Tuple
import pygame as pg
from CONFIG_JOGO import ConfigJogo
from personagem import Personagem
from lista_personagens import *
from Cena_Selecao1 import *

from Cronometro import *
from ataque_fisico import *
from level import Level


class CenaPrincipal:
    def __init__(self, tela:pg.Surface, per_1:Personagem, per_2:Personagem):
        self.indice_1=per_1
        self.indice_2=per_2
        self.tela = tela
        self.status=stats()
        self.player_1=self.status.lista_3[per_1]
        self.player_2=self.status.lista_3[per_2]
        self.player_1.posicao=(ConfigJogo.LARGURA_TELA*.25, ConfigJogo.ALTURA_TELA//2)
        self.player_2.posicao=(ConfigJogo.LARGURA_TELA*.75, ConfigJogo.ALTURA_TELA//2)
        self.fim = False
        self.cronometro_1=cronometro()
        self.cronometro_2=cronometro()
        self.cronometro_ataque_1=cronometro()
        self.cronometro_ataque_2=cronometro()
        self.cronometro_final=cronometro()
        self.vida_1=self.player_1.vida
        self.vida_2=self.player_2.vida
        self.velocidade_1=self.player_1.velocidade
        self.velocidade_2=self.player_2.velocidade
        self.level = Level('gelo.tmx', tela)

    def rodar(self):
        while not self.fim:
            self.Vitoria()
            self.desenha()
            self.tratamento_eventos()
            self.atualiza_estado()

    def tratamento_eventos(self):
        for event in pg.event.get():
            
            if (event.type == pg.QUIT):
                sys.exit(0)
            if (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE) or \
                    (pg.key.get_pressed()[pg.K_ESCAPE]):         
                self.fim = True
                ConfigJogo.Tela=1
                self.player_1.vida=self.vida_1
                self.player_2.vida=self.vida_2
               
                
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
        self.tela.fill('black')
        self.level.run()
        self.desenha_tempo()
        self.ataca_player_1()
        self.ataca_player_2()
        self.player_2.desenha(self.tela).draw(self.tela)
        self.player_1.desenha(self.tela).draw(self.tela)
        
               
        pg.display.flip()
    def ataca_player_1(self):
                
            if  pg.key.get_pressed()[pg.K_z] and self.cronometro_1.tempo_passado()>2 :

                    self.player_1.ataque[1].dano(self.tela, self.player_1, self.player_2, self.level)
                    self.player_1.ataque[1].tempo()
                    if  self.player_1.ataque[1].termina==1:
                        self.player_1.ataque[1].resetar_posicao(self.player_1)
                        self.cronometro_1.reset()
                
            if  pg.key.get_pressed()[pg.K_q] and self.cronometro_ataque_1.tempo_passado()>1.5 :
                    self.player_1.ataque[0].dano(self.tela, self.player_1, self.player_2, self.velocidade_2)
                    self.player_1.ataque[0].tempo()
                    if self.player_1.ataque[0].termina==1:
                        self.cronometro_ataque_1.reset() 
                        self.player_1.ataque[0].reset() 
    def ataca_player_2(self):   
                
            if  pg.key.get_pressed()[pg.K_o] and self.cronometro_ataque_2.tempo_passado()>1.5 :
                    self.player_2.ataque[0].dano(self.tela, self.player_2, self.player_1, self.velocidade_1)
                    self.player_2.ataque[0].tempo()
                    if self.player_2.ataque[0].termina==1:
                        self.cronometro_ataque_2.reset()
                        self.player_2.ataque[0].reset()

            if  pg.key.get_pressed()[pg.K_p] and self.cronometro_2.tempo_passado()>2  :
                    self.player_2.ataque[1].dano(self.tela, self.player_2, self.player_1, self.level)
                    self.player_2.ataque[1].tempo()
                    if  self.player_2.ataque[1].termina==1:
                        self.player_2.ataque[1].resetar_posicao(self.player_2)
                        self.cronometro_2.reset()
    def desenha_tempo(self):
        tempo=ConfigJogo.DURACAO_PARTIDA-self.cronometro_final.tempo_passado()
        font_subtitulo = pg.font.SysFont(None, ConfigJogo.Fonte_HISTORIA)
        self.subtitulo = font_subtitulo.render(
          f' {tempo:.0f}', True, ConfigJogo.COR_TITULO)
        px = ConfigJogo.LARGURA_TELA // 2 - self.subtitulo.get_size()[0] // 2
        py = (0.3 * ConfigJogo.ALTURA_TELA // 2)
        self.tela.blit(self.subtitulo, (px, py))
    def Vitoria(self)->int:
        if self.player_2.vida<=0:
                indice_vitoria=1
                self.fim = True
                ConfigJogo.Tela=6
                return indice_vitoria
        if self.player_1.vida<=0:
                indice_vitoria=2
                self.fim = True
                ConfigJogo.Tela=6
                return indice_vitoria
        if self.cronometro_final.tempo_passado()>=180:
                indice_vitoria=3
                self.fim = True
                ConfigJogo.Tela=6
                return indice_vitoria
    
           
           
           
            
                   


   

   