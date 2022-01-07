import pygame as pg
import sys
import os
from settings import *
from characters import *
from shop import *
from textbox import*
from inventory import *
from battle import *
import pygbutton
from map import *

# TODO LIST
# 1. SHOP
    # a. Render image and text file
    # b. Add an interactable NPC
    # c. Display donut images 
# 2. Combat System
    # a. Correct alingment and coordinates 
    # b. Defend/Items
    # c. Polish animations/sounds

class Game:
    def __init__(self, map):
        pg.init()
        self.map=map
        # Set screen settings
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        # Clock handles how fast the game moves, can vary with FPS variables
        self.clock = pg.time.Clock()
        self.current_map = 'Town'
        self.main_menu_pictures = ['title_placeholder.png', 'title_placeholder1.png']
        self.index = 0
        self.image = self.main_menu_pictures[self.index]
        self.update_time = pg.time.get_ticks()
        self.bg = pg.image.load(os.path.join(
            IMAGE_FOLDER, 'town_map.png'))
        # Allow the user to hold the key down and it will auto repeat that key every .5 seconds
        pg.key.set_repeat(500, 100)
        self.loading_shop = False  # SHOP MAP TRANSITION
        self.main_menu_running = True
        self.inventory_open = False
        self.battling = False
        self.map = Map('map.txt')

    def new(self):
        # Grab all the sprites and place them on the screen upon starting
        self.all_sprites = pg.sprite.Group()
        self.player_sprite = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.npcs = pg.sprite.Group()
        self.textboxes = pg.sprite.Group()
        for row, tiles in enumerate(self.map.map_data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    self.wall = Wall(self, col, row)
                if tile == 'P':
                    self.player = Player(self, col, row)
                if tile == 'N':
                    NPC(self, col, row, OLD_MAN, None,
                        OLD_MAN_TEXT, OLD_MAN_PORTRAIT, (16,16), False)
                if tile == 'D':
                    NPC(self,
                        col, row, BRONUT1, None,
                        BRONUT_TEXT, BRONUT_PORTRAIT, (1080, 1440), True)
                    
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

    def draw(self):
        # Draw everything onto the screen
        self.screen.fill(BGCOLOR)
        pg.display.set_caption(str(self.player.x) + ',' + str(self.player.y))
        if self.battling:
            Battle(self)
        if self.loading_shop:
            self.map.clear_map()
            self.map = Map('shop.txt')
            Shop(self)
            self.all_sprites.draw(self.screen)
        if self.loading_shop == False:  
            self.screen.blit(self.bg, (0, 0))
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
                elif event.key == pg.K_i:
                    self.inventory = Inventory(self)
                elif event.key == pg.K_r:
                    self.player.change_character()
                if event.key == pg.K_LEFT:
                    self.player.move(dx=-1)
                if event.key == pg.K_RIGHT:
                    self.player.move(dx=1)
                if event.key == pg.K_UP:
                    self.player.move(dy=-1)
                if event.key == pg.K_DOWN:
                    self.player.move(dy=1)
              
    def start_game(self):
        self.clock.tick(200)
        self.screen.blit(BACKGROUND, (0, 0))
        pg.display.update()
        self.main_menu_conversations = ['But CJ, how can I fight without my stylish cardigan?', "Tony, it's not what is on the outside that counts. Besides, you're already plenty stylish!",
            "Yeah, Tony. We have to go and fight the yeti before he has a chance to attack the village.", "Let's check with that man over there. If he hasn't seen it then we'll just have to fight without it."]
        self.main_menu_portraits = [TONY, CJ, RYAN, JR]
        self.textbox = TextBox(self, None, None, (16,16))
        for i in range(len((self.main_menu_conversations))):
            self.textbox.dialog_box.set_text(self.main_menu_conversations[i])
            self.textbox.dialog_box.set_portrait(
                self.main_menu_portraits[i], (16, 16))
            self.textbox.display_textbox()
        self.main_menu_running = False

    def show_start_screen(self):
        self.time_counter = 0
        self.image_1 = pg.image.load(os.path.join(IMAGE_FOLDER, "Animation.png"))
        self.image_2 = pg.image.load(os.path.join(IMAGE_FOLDER, "Animation2.png"))
        self.image_3 = pg.image.load(os.path.join(IMAGE_FOLDER, "Animation3.png"))
        self.image_4 = pg.image.load(os.path.join(IMAGE_FOLDER, "Animation4.png"))
        self.image_5 = pg.image.load(os.path.join(IMAGE_FOLDER, "Animation5.png"))
        
        # new_game = pg.image.load(os.path.join(IMAGE_FOLDER, "New game button.png"))
        self.title = pg.image.load(os.path.join(IMAGE_FOLDER, "RJCT Adventure title.png"))
        
        # Buttons
        self.main_menu_button = pygbutton.PygButton((100,675,200,50), normal = os.path.join(IMAGE_FOLDER, "New_game_button.png"))
        self.load_game_button = pygbutton.PygButton((325,675,200,50), normal = os.path.join(IMAGE_FOLDER, "Load game button.png"))
        self.exit_game_button = pygbutton.PygButton((525,700,200,50), normal = os.path.join(IMAGE_FOLDER, "Exit game button.png"))
        self.list_of_buttons =  [self.main_menu_button, self.load_game_button, self.exit_game_button]

        animate = True
        while animate:
            pg.time.Clock().tick(60)
            the_clock_tick = self.clock.tick()
            self.time_counter += the_clock_tick

            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    pg.quit()
                    break
            if self.time_counter < 250:
                self.screen.blit(self.image_1, (0,0))
            if self.time_counter >= 250 and self.time_counter < 500:
                self.screen.blit(self.image_2, (0,0))
            if self.time_counter >= 500 and self.time_counter < 750:
                self.screen.blit(self.image_3, (0,0))
            if self.time_counter >= 750 and self.time_counter < 1000:
                self.screen.blit(self.image_4, (0,0))
            if self.time_counter >= 1000 and self.time_counter < 1250:
                self.screen.blit(self.image_5, (0,0))
            if self.time_counter >= 1250:
                self.time_counter = 0

            if 'click' in self.main_menu_button.handleEvent(event):
                self.start_game()  
                animate = False
            if 'click' in self.load_game_button.handleEvent(event):
                pg.quit()
            if 'click' in self.exit_game_button.handleEvent(event):
                pg.quit()
                    
            for button in self.list_of_buttons:
                button.draw(self.screen)
            self.screen.blit(self.title, (220,0))
            pg.display.flip()
            
         
    def show_go_screen(self):
        # Maybe the confirmation to start game?
        print('END LOOP')

# create the game object
g = Game('map.txt')

while g.main_menu_running:
    # mixer.init()
    # mixer.music.load('maps/MainMenuMusic.mp3')
    # mixer.music.play(-1) 
    g.show_start_screen() 
    while not g.main_menu_running:
        g.new()
        g.run()
        g.show_go_screen()