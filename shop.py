import pygame as pg
from settings import *
from characters import *
import os 
from map import *

class Shop():
    def __init__(self, game):
        pg.init()
        self.game = game
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption('RJCT Shop')
        self.npc = SHOP_NPC
        self.bg = pg.image.load(os.path.join(IMAGE_FOLDER, 'shop_map_remix.png'))
        self.game.screen.blit(self.bg, (0,0))
        self.map = Map('shop.txt')
        
        for row, tiles in enumerate(self.map.map_data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    self.wall = Wall(self, col, row)
                if tile == 'P':
                    self.player = Player(self, col, row)