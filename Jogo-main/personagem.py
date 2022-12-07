
import pygame as pg
from Cronometro import cronometro
from CONFIG_JOGO import ConfigJogo
from typing import Tuple
from sprite import Jogador



class Personagem:
    def __init__(self, nome:str, vida:float, velocidade:float, dano_fisico:int, dano_magico:int, ataque:Tuple):
        self.nome=nome
        self.vida=vida
        self.dano_fisico=dano_fisico
        self.dano_magico=dano_magico
        self.posicao=(0, 0)
        self.ataque=ataque
        self.velocidade=velocidade
        self.velocidade_x_muda = velocidade
        self.velocidade_y_muda = velocidade
        self.velocidade_x=0
        self.velocidade_y=0
        self.direcao=0
        self.cronometro=cronometro()

    def mover_para_cima(self):
        self.velocidade_y = -self.velocidade_y_muda

    def mover_para_baixo(self):
        self.velocidade_y = self.velocidade_y_muda

    def mover_para_direita(self):
        self.velocidade_x = self.velocidade_x_muda
        self.direcao=0
    def mover_para_esquerda(self):
        self.velocidade_x = -self.velocidade_x_muda
        self.direcao=1

    def para_x(self):
        self.velocidade_x = 0
       
    def para_y(self):
        self.velocidade_y = 0

    def atualizar_posicao(self):
        x, y = self.posicao
        novo_y = y + self.velocidade_y
        novo_x = x + self.velocidade_x

        if ((novo_y >= 0) and \
                ((novo_y + ConfigJogo.tamanho_per) <= ConfigJogo.ALTURA_TELA)) and \
                    ((novo_x>=0) and ((novo_x +ConfigJogo.tamanho_per)<=ConfigJogo.LARGURA_TELA)):
            if not ((novo_y<128 and novo_y>64-ConfigJogo.tamanho_per)  and (novo_x>128-ConfigJogo.tamanho_per and novo_x<224)):
                if not ((novo_y<128 and novo_y>64-ConfigJogo.tamanho_per)  and (novo_x>1056-ConfigJogo.tamanho_per and novo_x<1152)):
                    if not ((novo_y<576 and novo_y>512-ConfigJogo.tamanho_per)  and (novo_x>128-ConfigJogo.tamanho_per and novo_x<224)):
                        if not ((novo_y<576 and novo_y>512-ConfigJogo.tamanho_per)  and (novo_x>1056-ConfigJogo.tamanho_per and novo_x<1152)):
                            if not ((novo_y<576 and novo_y>448-ConfigJogo.tamanho_per)  and (novo_x>448-ConfigJogo.tamanho_per and novo_x<480)):
                                if not ((novo_y<576 and novo_y>448-ConfigJogo.tamanho_per)  and (novo_x>800-ConfigJogo.tamanho_per and novo_x<832)):
                                    if not ((novo_y<192 and novo_y>64-ConfigJogo.tamanho_per)  and (novo_x>448-ConfigJogo.tamanho_per and novo_x<480)):
                                        if not ((novo_y<192 and novo_y>64-ConfigJogo.tamanho_per)  and (novo_x>800-ConfigJogo.tamanho_per and novo_x<832)):
                                            self.posicao = (novo_x, novo_y)

    def desenha(self, tela:pg.Surface):
        x = self.posicao[0]
        y = self.posicao[1]
        l = ConfigJogo.tamanho_per
        a = ConfigJogo.tamanho_per
        
        sprites = pg.sprite.Group()
        personagem = Jogador(self.nome, x, y, self.direcao)
        sprites.add(personagem)
       

        font_subtitulo = pg.font.SysFont(None, ConfigJogo.Fonte_HISTORIA)
        self.subtitulo = font_subtitulo.render(
          f' {self.vida}', True, ConfigJogo.COR_TITULO)
        tela.blit(self.subtitulo, (x-2, y-ConfigJogo.meiotamanho_per-12))
        return sprites
    
       
    
    
   
        
                
        
    