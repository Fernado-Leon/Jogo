import pygame as pg
from CONFIG_JOGO import ConfigJogo
from Cena_inicial import Cenainicial
from Cena_historia import Historia
from Cena_Selecao1 import *
from Cena_principal import *
from cena_vitoria import *
from lista_personagens import stats


class guerrafria:
    def __init__(self):
        pg.init()
        
       
    def rodar(self):

        ConfigJogo.Tela = 1
        while True:
            if ConfigJogo.Tela==1:
                pg.mixer.music.stop()
                ConfigJogo.LARGURA_TELA = 1280
                ConfigJogo.ALTURA_TELA = 640
                self.tela = pg.display.set_mode((
            ConfigJogo.LARGURA_TELA,
            ConfigJogo.ALTURA_TELA
            ))
                cena = Cenainicial(self.tela)        
                cena.rodar()
            if ConfigJogo.Tela==2:
                cena=Historia(self.tela)
                cena.rodar()
            if ConfigJogo.Tela==3:
                cena=CenaSelecao1(self.tela, 'JOGADOR 1', 'red', 4)
                cena.rodar()
                indice_1=cena.escolha()
            if ConfigJogo.Tela==4:
                cena=CenaSelecao1(self.tela, 'JOGADOR 2', 'blue', 5)
                cena.rodar()
                indice_2=cena.escolha()
            if ConfigJogo.Tela==5:
               
                ConfigJogo.LARGURA_TELA=1280
                ConfigJogo.ALTURA_TELA=640
                self.tela = pg.display.set_mode((
            ConfigJogo.LARGURA_TELA,
            ConfigJogo.ALTURA_TELA
            ))
                cena=CenaPrincipal(self.tela, indice_1, indice_2)
                        #volume varia de 0 a 1
                pg.mixer.music.set_volume(0.5)
                #baixa o arquivo
                pg.mixer.music.load('m1.wav')
                # toca a musica repetidammente
                pg.mixer.music.play(-1)
                
                cena.rodar()
                indice_vitoria=cena.Vitoria()
                
            if ConfigJogo.Tela==6:
                cena=Cenavitoria(self.tela, indice_vitoria)
                cena.rodar()
                
            
            
            

       