import pygame as pg
from constantes import Constantes
from cena_inicial import Cenainicial
from cena_historia import Historia
from cena_selecao1 import *
from cena_selecao2 import *
from cena_principal import *


class guerrafria:
    def __init__(self):
        pg.init()

        self.tela = pg.display.set_mode((
            Constantes.LARGURA_TELA,
            Constantes.ALTURA_TELA
        ))

        # fernando: adiciona titulo o nome na pagina 
        pg.display.set_caption('Guerra Fria')


    def rodar(self):
        Constantes.Tela=1
        while True:
            if Constantes.Tela==1:
                cena = Cenainicial(self.tela)        
                cena.rodar()
            if Constantes.Tela==2:
                cena=Historia(self.tela)
                cena.rodar()
            if Constantes.Tela==3:
                cena=CenaSelecao1(self.tela)
                cena.rodar()
                indice_1=cena.escolha()
            if Constantes.Tela==4:
                cena=CenaSelecao2(self.tela)
                cena.rodar()
                indice_2=cena.escolha()
            if Constantes.Tela==5:
                
                cena=CenaPrincipal(self.tela, indice_1, indice_2)
                cena.rodar()
            
            
            

       