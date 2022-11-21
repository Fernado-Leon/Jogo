
import pygame as pg
from CONFIG_JOGO import ConfigJogo
from personagem import Personagem
from ataque_fisico import *
from ataque_magico import magia
from invocar import minion
from tirambasso import tirinho
from teleporte import dash

tiro=tirinho()
ataque_perto=fisico()
soldado_1=Personagem("soldado", 300, 1, 20, 0, (1200//2,900*.75 ), (ataque_perto))
soldado_2=Personagem("soldado", 300, 1, 20, 0, (1200//2,900//4 ), (ataque_perto))
ataque_invocar=minion(soldado_1, soldado_2)

STALIN=Personagem("STALIN", 2000, 0.8, 35, 150, (1200//4,900//2 ),(ataque_invocar, magia()))
GORBACHOV=Personagem("GORBACHOV", 3600, 0.2, 40, 0, (1200//4,900//2 ),(ataque_perto, magia()))
IVAN_DRAGO=Personagem("IVAN DRAGO", 3000, 1, 40, 0, (1200//4,900//2 ),(ataque_perto, magia()))
RASPUTIN=Personagem("RASPUTIN", 1600, 1, 2, 190, (1200//4,900//2 ),(ataque_perto, magia()))
RAMBO=Personagem("RAMBO", 3000, 1.2, 40, 0, (1200*0.75,900//2 ),(ataque_perto, magia()))
MUHAMMAD_ALI=Personagem("MUHAMMAD ALI", 1800, 6, 50, 0, (1200*0.75,900//2 ),(ataque_perto, dash()))
JESSE_JAMES=Personagem("JESSE JAMES", 2800, 1.2, 50, 120, (1200*0.75,900//2), (ataque_perto, tiro))
JOHN_F_KENNEDY=Personagem("JOHN F KENNEDY", 1000, .8, 50, 30, (1200*0.75,900//2),(ataque_invocar, magia()))
soldado=Personagem=("soldado", 300, 1, 20, 0, (1200//2,900//2 ), (ataque_perto))


lista_1=[STALIN, GORBACHOV , IVAN_DRAGO, RASPUTIN]
lista_2=[MUHAMMAD_ALI, JESSE_JAMES, RAMBO, JOHN_F_KENNEDY]
#modelo lista so de role=[vida, velocidade, dano_fisico, dano_magico, posicao]


