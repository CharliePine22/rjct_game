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
NAVY = (8, 34, 79)

# game settings
WIDTH = 800 
HEIGHT = 800
FPS = 60
TITLE = "RJCT RPG"
pg.font.init()
MAIN_FONT = pg.font.SysFont('Arial', 20)

# Folders to get to images
GAME_FOLDER = os.path.dirname(__file__)
IMAGE_FOLDER = os.path.join(GAME_FOLDER, 'maps')
BACKGROUND = pg.image.load(os.path.join(IMAGE_FOLDER, 'title_placeholder.png'))
TOWN_BG = pg.image.load(os.path.join(IMAGE_FOLDER, 'town_map.png'))
INVENTORY_PIC = pg.image.load(os.path.join(IMAGE_FOLDER, 'Inventory_UI.png'))
BATTLE_BG = pg.image.load(os.path.join(IMAGE_FOLDER, 'BattleBG.png'))
VICTORY_BG = pg.image.load(os.path.join(IMAGE_FOLDER, 'Congrats.png'))

#RJCT Settings
RYAN = 'maps/RJCT_RYAN.png'
JR = 'maps/RJCT_JR.png'
CJ = 'maps/RJCT_CJ.png'
TONY = 'maps/RJCT_TONY.png'
TONY_CARDIGAN = pg.image.load('maps/TonyCardigan.png')

# Old man NPC settings
OLD_MAN = pg.image.load(os.path.join(IMAGE_FOLDER, "npc_test.png"))
OLD_MAN_PORTRAIT = 'maps/old_man_thumbnail.png'
OLD_MAN_PATH = [(554, 350), (574, 350), (534,350), (544, 350)] #tuples are destination coordinates
OLD_MAN_TEXT = 'Greetings adventurers, welcome to Shiverbell. I would love to give you a proper tour, but right now, our town is being threatened by the mountain Yeti. Think you guys can handle it?'

# Tony bronut settings, Get both images for aniamtion
BRONUT1 = pg.image.load(os.path.join(IMAGE_FOLDER, "Asperite_Bronut1.png"))
BRONUT1 = pg.transform.scale(BRONUT1, (75, 75))
BRONUT2 = pg.image.load(os.path.join(IMAGE_FOLDER, "Asperite_Bronut2.png"))
BRONUT2 = pg.transform.scale(BRONUT2, (75, 75))
BRONUT_PORTRAIT = 'maps/bronut_portrait.png'
BRONUT_PATH = [(400, 600), (500, 600), (456, 547), (450,500)]
BRONUT_TEXT = 'PLEASE DONT EAT ME PLEASE, I JUST WANNA DANCE IN PEACE!'
BGCOLOR = WHITE

# Shopkeeper NPC
SHOP_NPC = pg.image.load(os.path.join(IMAGE_FOLDER, 'sprite_0.png'))
TEST = pg.image.load(os.path.join(IMAGE_FOLDER, 'snow_template1.jpg'))
# Player Sprite Settings

PLAYER_SPEED = 150
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)

# NPC Sprite Settings
NPC_SPEED = 50
NPC_HIT_RECT = pg.Rect(0, 0, 30, 30)

# Set how many tiles and how large each tile takes
TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE