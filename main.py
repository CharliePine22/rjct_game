import pygame as pg
import sys
import os
from settings import *
from characters import *
from textbox import *

class Game:
    def __init__(self):
        pg.init()
        # Set screen settings
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        # Clock handles how fast the game moves, can vary with FPS variables
        self.clock = pg.time.Clock()
        self.bg = pg.image.load(os.path.join(IMAGE_FOLDER, 'Background_Placeholder.png'))
        # Allow the user to hold the key down and it will auto repeat that key every .5 seconds
        pg.key.set_repeat(500, 100)
        self.load_map()

    def load_map(self):
        # Grab map boundries from text file
        game_folder = os.path.dirname(__file__)
        map_folder = os.path.join(game_folder, 'maps')
        self.map_data = []
        with open(os.path.join(map_folder, 'map.txt'), 'rt') as f:
            for line in f:
                self.map_data.append(line)      

    def new(self):
        # Grab all the sprites and place them on the screen upon starting
        self.all_sprites = pg.sprite.Group()
        self.player_sprite = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.npcs = pg.sprite.Group()
        self.textboxes = pg.sprite.Group()
        
        # Loop through map.txt file to get access to rows and columns
        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)
                if tile == 'P':
                    self.player = Player(self, col, row)
                if tile == 'N':
                    NPC(self, col, row, OLD_MAN, OLD_MAN_PATH, OLD_MAN_TEXT, 'old_man_thumbnail.png')
                if tile == 'D':
                    NPC(self, col, row, BRONUT1, None, BRONUT_TEXT, 'Asperite_Bronut2.png')
                          
    def run(self):
        # Game loop, if self.playing is changed to false, the game stops
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def load_data(self):
        # Potentially load saved data
        pass
    
    def save_data(self):
        # Potentially save data
        pass

    def update(self):
        # update each sprite appropriately
        self.all_sprites.update()

    def draw_grid(self):
        pg.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        # Draw tiles on the screen to make a grid
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        # Draw everything onto the screen
        self.screen.fill(BGCOLOR)
        self.screen.blit(self.bg, (0,0))
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            # If the user is quitting
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                # Allow user to quit via ESC key
                if event.key == pg.K_ESCAPE:
                    self.quit()

    def show_start_screen(self):
        # Ryans sexy ass menu design
        pass

    def show_go_screen(self):
        # Maybe the confirmation to start game?
        pass

# create the game object
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()