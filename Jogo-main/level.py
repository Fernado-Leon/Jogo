import pygame
from suport import import_csv_layout, import_cut_graphics
from CONFIG_JOGO import ConfigJogo
from tiles import Tile, StaticTile




class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface

        terrain_layout = import_csv_layout('neve.csv')
        self.terrain_sprites = self.creat_tile_group(terrain_layout,'neve.csv')
    
    def creat_tile_group(self, layout, type):
        sprite_group = pygame.sprite.Group()

        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                x = col_index * ConfigJogo.TILE_SIZE
                y = row_index * ConfigJogo.TILE_SIZE

                terrain_tile_list = import_cut_graphics("IceTileset.png")
                tile_surface = terrain_tile_list[int(val)]
                sprite = StaticTile(ConfigJogo.TILE_SIZE, x, y, tile_surface)
                sprite_group.add(sprite)

        return sprite_group

    
    def run(self):

        self.terrain_sprites.draw(self.display_surface)
        self.terrain_sprites.update(0)