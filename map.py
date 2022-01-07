import pygame as pg
from settings import *
from characters import *

class Map():
    def __init__(self, file):
        pg.init()
        self.map_data = []
        self.file = file
        self.load_map()
        
    def load_map(self):  
        # Grab map boundries from text file
        with open(os.path.join(IMAGE_FOLDER, self.file), 'rt') as f:
            for line in f:
                self.map_data.append(line)

    # def display_map(self):
    #     for row, tiles in enumerate(self.map_data):
    #         for col, tile in enumerate(tiles):
    #             if tile == '1':
    #                 self.wall = Wall(self, col, row)
    #             if tile == 'P':
    #                 self.player = Player(self, col, row)
    #             if tile == 'N':
    #                 NPC(self, col, row, OLD_MAN, OLD_MAN_PATH,
    #                     OLD_MAN_TEXT, OLD_MAN_PORTRAIT, False)
    #             if tile == 'D':
    #                 NPC(self,
    #                     col, row, BRONUT1, None,
    #                     BRONUT_TEXT, BRONUT_PORTRAIT, True)


    def clear_map(self):
        self.map_data = []