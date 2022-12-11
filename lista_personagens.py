
import pygame as pg
from CONFIG_JOGO import ConfigJogo
from personagem import Personagem
from ataque_fisico import *
from ataque_magico import magia
from invocar import minion
from tirambasso import tirinho
from teleporte import dash
from curar import cura
class stats:
    def __init__(self):
        self.tiro=tirinho()
        self.ataque_perto=fisico()
        self.soldado_1=Personagem("soldado", 300, 1, 20, 0,  (self.ataque_perto))
        self.soldado_2=Personagem("soldado", 300, 1, 20, 0, (self.ataque_perto))
        self.soldado_3=Personagem("soldado", 300, 1, 20, 0,  (self.ataque_perto))
        self.ataque_invocar=minion([self.soldado_1, self.soldado_2, self.soldado_3])
        self.STALIN=Personagem("STALIN", 2000, 2, 35, 150, (self.ataque_invocar, magia()))
        self.GORBACHOV=Personagem("GORBACHOV", 2900, 1.5, 40, 0, (self.ataque_perto, magia()))
        self.IVAN_DRAGO=Personagem("IVAN DRAGO", 3000, 2.5, 40, 0, (self.ataque_perto, self.tiro))
        self.RASPUTIN=Personagem("RASPUTIN", 1500, 1.5, 2, 220, (cura(), magia()))
        self.RAMBO=Personagem("RAMBO", 3000, 2.5, 40, 0,(self.ataque_perto, self.tiro))
        self.MUHAMMAD_ALI=Personagem("MUHAMMAD ALI", 1800, 3, 50, 0,(self.ataque_perto, dash()))
        self.JESSE_JAMES=Personagem("JESSE JAMES", 2800, 2.5, 50, 120,  (self.ataque_perto, self.tiro))
        self.JOHN_F_KENNEDY=Personagem("JOHN F KENNEDY", 1000, 1.5, 50, 30, (self.ataque_invocar, magia()))
        self.lista_3 = [self.STALIN, self.GORBACHOV , self.IVAN_DRAGO, self.RASPUTIN, self.MUHAMMAD_ALI, self.JESSE_JAMES, self.RAMBO, self.JOHN_F_KENNEDY]
       
    def reseta_tudo(self):
        self.tiro=tirinho()
        self.ataque_perto=fisico()
        self.soldado_1=Personagem("soldado", 300, 1, 20, 0,  (self.ataque_perto))
        self.soldado_2=Personagem("soldado", 300, 1, 20, 0, (self.ataque_perto))
        self.soldado_3=Personagem("soldado", 300, 1, 20, 0,  (self.ataque_perto))
        self.ataque_invocar=minion([self.soldado_1, self.soldado_2, self.soldado_3])
        self.STALIN=Personagem("STALIN", 2000, 2, 35, 150, (self.ataque_invocar, magia()))
        self.GORBACHOV=Personagem("GORBACHOV", 2900, 1.5, 40, 0, (self.ataque_perto, magia()))
        self.IVAN_DRAGO=Personagem("IVAN DRAGO", 3000, 2.5, 40, 0, (self.ataque_perto, self.tiro))
        self.RASPUTIN=Personagem("RASPUTIN", 1500, 1.5, 2, 220, (cura(), magia()))
        self.RAMBO=Personagem("RAMBO", 3000, 2.5, 40, 0,(self.ataque_perto, self.tiro))
        self.MUHAMMAD_ALI=Personagem("MUHAMMAD ALI", 1800, 3, 50, 0,(self.ataque_perto, dash()))
        self.JESSE_JAMES=Personagem("JESSE JAMES", 2800, 2.5, 50, 120,  (self.ataque_perto, self.tiro))
        self.JOHN_F_KENNEDY=Personagem("JOHN F KENNEDY", 1000, 1.5, 50, 30, (self.ataque_invocar, magia()))
        self.lista_3 = [self.STALIN, self.GORBACHOV , self.IVAN_DRAGO, self.RASPUTIN, self.MUHAMMAD_ALI, self.JESSE_JAMES, self.RAMBO, self.JOHN_F_KENNEDY]
       
       
        



