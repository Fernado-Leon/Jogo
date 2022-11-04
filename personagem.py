from typing import Tuple
import pygame as pg

from CONFIG_JOGO import ConfigJogo



class Personagem:
    def __init__(self, nome, vida, velocidade, dano_fisico, dano_magico, posicao):
        self.nome=nome
        self.vida=vida
        self.dano_fisico=dano_fisico
        self.dano_magico=dano_magico
        self.posicao=posicao
        self.posicao = posicao
        self.velocidade_x_muda = velocidade
        self.velocidade_y_muda = velocidade
        self.velocidade_x=0
        self.velocidade_y=0
    def mover_para_cima(self):
        self.velocidade_y = -self.velocidade_y_muda

    def mover_para_baixo(self):
        self.velocidade_y = self.velocidade_y_muda

    def mover_para_direita(self):
        self.velocidade_x = self.velocidade_x_muda
    def mover_para_esquerda(self):
        self.velocidade_x = -self.velocidade_x_muda

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
            self.posicao = (novo_x, novo_y)

    def desenha(self, tela):
        x = self.posicao[0]
        y = self.posicao[1]
        l = ConfigJogo.tamanho_per
        a = ConfigJogo.tamanho_per
        pg.draw.rect(
            tela,
            (0,0,0),
            pg.rect.Rect(x, y, l, a)
        )

    def position(self) -> Tuple[float, float, float, float]:
        return self.posicao + (ConfigJogo.tamanho_per, ConfigJogo.tamanho_per)
