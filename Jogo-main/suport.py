from csv import reader
import pygame
from CONFIG_JOGO import ConfigJogo

def import_csv_layout(path):
    terrain_map = []
    with open(path) as map:
        level = reader(map, delimiter = ',')
        for row in level:
            terrain_map.append(list(row))
        return terrain_map

cut_tiles = []
def import_cut_graphics(path):
    surface = pygame.image.load(path).convert_alpha()
    tile_num_x = int(surface.get_size()[0] // ConfigJogo.TILE_SIZE)
    tile_num_y = int(surface.get_size()[1] // ConfigJogo.TILE_SIZE)
    
    for row in range(tile_num_y):
        for col in range(tile_num_x):
            x = col * ConfigJogo.TILE_SIZE
            y = row * ConfigJogo.TILE_SIZE
            new_surf = pygame.Surface((ConfigJogo.TILE_SIZE, ConfigJogo.TILE_SIZE))
            new_surf.blit(surface, (0,0), pygame.Rect(x, y, ConfigJogo.TILE_SIZE, ConfigJogo.TILE_SIZE))
            cut_tiles.append(new_surf)
    
    return cut_tiles

