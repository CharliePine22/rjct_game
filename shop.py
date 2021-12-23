import pygame as pg
from settings import *
from characters import *
import os 

class Shop():
    def __init__(self, game):
        pg.init()
        self.game = game
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption('RJCT Shop')
        self.npc = SHOP_NPC
        self.bg = pg.image.load(os.path.join(IMAGE_FOLDER, 'shop_placeholder.png'))
        self.load_store()
        
    def load_store(self):
        self.map_data = []
        with open(os.path.join(IMAGE_FOLDER, 'shop.txt'), 'rt') as f:
            for line in f:
                self.map_data.append(line)
    
    def display_store(self):
        self.all_sprites = pg.sprite.Group()
        self.player_sprite = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.npcs = pg.sprite.Group()
        self.textboxes = pg.sprite.Group()
        
        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    pass