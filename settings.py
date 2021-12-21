import pygame as pg
import os 

# Set colors for potential backgrounds(green for grass white for clouds etc.)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
BROWN = (165, 42, 42)
RED = (255, 0, 0)
YELLOW = (255, 242, 0)

# game settings
WIDTH = 800 
HEIGHT = 800
FPS = 60
TITLE = "RJCT RPG"

# Folders to get to images
GAME_FOLDER = os.path.dirname(__file__)
IMAGE_FOLDER = os.path.join(GAME_FOLDER, 'maps')
# Old man NPC settings
OLD_MAN = pg.image.load(os.path.join(IMAGE_FOLDER, "npc_test.png"))
OLD_MAN_PATH = [(554, 352), (564, 400), (534,362), (544, 352)] #tuples are destination coordinates
OLD_MAN_TEXT = 'Greetings adventurers, welcome to Shiverbell. I would love to give you a proper tour, but right now, our town is being threatened by the mountain Yeti. If you encounter it, be sure to have a cardigan on you, here take this one, and be careful!'
# Tony bronut settings
BRONUT1 = pg.image.load(os.path.join(IMAGE_FOLDER, "Asperite_Bronut1.png"))
BRONUT1 = pg.transform.scale(BRONUT1, (75, 75))
BRONUT_TEXT = 'PLEASE DONT EAT ME PLEASE, I JUST WANNA DANCE IN PEACE!'
BRONUT_PATH = [(400, 600), (500, 600), (456, 547), (450,500)]
BGCOLOR = WHITE

# Player Sprite Settings
PLAYER_SPEED = 150
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)

# NPC Sprite Settings
NPC_SPEED = 100
NPC_HIT_RECT = pg.Rect(0, 0, 30, 30)

# Set how many tiles and how large each tile takes
TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE