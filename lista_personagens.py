
import pygame as pg
from constantes import Constantes
from personagem import Personagem

STALIN=Personagem("STALIN", 2000, 0.8, 35, 150, (Constantes.LARGURA_TELA//4,Constantes.ALTURA_TELA//2 ))
GORBACHOV=Personagem("GORBACHOV", 2000, 0.2, 35, 150, (Constantes.LARGURA_TELA//4,Constantes.ALTURA_TELA//2 ))
IVAN_DRAGO=Personagem("IVAN DRAGO", 2000, 1, 35, 150, (Constantes.LARGURA_TELA//4,Constantes.ALTURA_TELA//2 ))
RASPUTIN=Personagem("RASPUTIN", 2000, 1.9, 35, 150, (Constantes.LARGURA_TELA//4,Constantes.ALTURA_TELA//2 ))
RAMBO=Personagem("RAMBO", 2500, 1.2, 50, 0, (Constantes.LARGURA_TELA*0.75,Constantes.ALTURA_TELA//2 ))
MUHAMMAD_ALI=Personagem("MUHAMMAD ALI", 2500, 6, 50, 0, (Constantes.LARGURA_TELA*0.75,Constantes.ALTURA_TELA//2 ))
JESSE_JAMES=Personagem("JESSE JAMES", 2500, 4, 50, 0, (Constantes.LARGURA_TELA*0.75,Constantes.ALTURA_TELA//2 ))
JOHN_F_KENNEDY=Personagem("JOHN F KENNEDY", 2500, .2, 50, 0, (Constantes.LARGURA_TELA*0.75,Constantes.ALTURA_TELA//2 ))



lista_1=[STALIN, GORBACHOV , IVAN_DRAGO, RASPUTIN]
lista_2=[MUHAMMAD_ALI, JESSE_JAMES, RAMBO, JOHN_F_KENNEDY]
#modelo lista so de role=[vida, velocidade, dano_fisico, dano_magico, posicao]


