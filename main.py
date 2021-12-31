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

# TODO LIST
# 1. Transitions/Lighting
# 2. Sounds
# 3. Textbox Confirmation
# 4. Shop Update
# 5. Housewives of Miami

class Game:
    def __init__(self):
        pg.init()
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
        self.time_counter = 0
        self.image_1 = pg.image.load(os.path.join(IMAGE_FOLDER, "Animation.png"))
        self.image_2 = pg.image.load(os.path.join(IMAGE_FOLDER, "Animation2.png"))
        self.image_3 = pg.image.load(os.path.join(IMAGE_FOLDER, "Animation3.png"))
        self.image_4 = pg.image.load(os.path.join(IMAGE_FOLDER, "Animation4.png"))
        self.image_5 = pg.image.load(os.path.join(IMAGE_FOLDER, "Animation5.png"))
        
        # new_game = pg.image.load(os.path.join(IMAGE_FOLDER, "New game button.png"))
        self.title = pg.image.load(os.path.join(IMAGE_FOLDER, "RJCT Adventure title.png"))

        # Buttons
        self.main_menu_button = pygbutton.PygButton((100,700,200,50), normal = os.path.join(IMAGE_FOLDER, "New_game_button.png"))
        self.load_game_button = pygbutton.PygButton((350,700,200,50), normal = os.path.join(IMAGE_FOLDER, "Load game button.png"))
        self.exit_game_button = pygbutton.PygButton((600,720,200,50), normal = os.path.join(IMAGE_FOLDER, "Exit game button.png"))
        self.list_of_buttons =  [self.main_menu_button, self.load_game_button, self.exit_game_button]

    def load_map(self, file):
        # Grab map boundries from text file
        self.map_data = []
        with open(os.path.join(IMAGE_FOLDER, file), 'rt') as f:
            for line in f:
                self.map_data.append(line)
        

    def new(self):
        # Grab all the sprites and place them on the screen upon starting
        self.all_sprites = pg.sprite.Group()
        self.player_sprite = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.npcs = pg.sprite.Group()
        self.textboxes = pg.sprite.Group()
        if not self.loading_shop:
            self.load_map('map.txt')
            # Loop through map.txt file to get access to rows and columns
            for row, tiles in enumerate(self.map_data):
                for col, tile in enumerate(tiles):
                    if tile == '1':
                        Wall(self, col, row)
                    if tile == 'P':
                        self.player = Player(self, col, row)
                    if tile == 'N':
                        NPC(self, col, row, OLD_MAN, OLD_MAN_PATH,
                            OLD_MAN_TEXT, OLD_MAN_PORTRAIT, False)
                    if tile == 'D':
                        NPC(self,
                            col, row, BRONUT1, None,
                            BRONUT_TEXT, BRONUT_PORTRAIT, True)
                        
    def new2(self):
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
        if self.battling:
            Battle(self)
        if self.loading_shop:
            print('SHOP')
            self.load_map('shop.txt')
            self.shop = Shop(self)
            for row, tiles in enumerate(self.map_data):
                for col, tile in enumerate(tiles):
                    if tile == '1':
                        Wall(self, col, row)
                    if tile == 'P':
                        self.player = Player(self, col, row)
            self.player_sprite.draw(self.screen)
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

    def start_game(self):
        self.clock.tick(200)
        self.screen.blit(BACKGROUND, (0, 0))
        pg.display.update()
        self.main_menu_conversations = ['But CJ, how can I fight without my stylish cardigan?', "Tony, it's not what is on the outside that counts. Besides, you're already plenty stylish!",
            "Yeah, Tony. We have to go and fight the yeti before he has a chance to attack the village.", "Let's check with that man over there. If he hasn't seen it then we'll just have to fight without it."]
        self.main_menu_portraits = [TONY, CJ, RYAN, JR]
        self.textbox = TextBox(self, None, None)
        for i in range(len((self.main_menu_conversations))):
            self.textbox.dialog_box.set_text(self.main_menu_conversations[i])
            self.textbox.dialog_box.set_portrait(
                self.main_menu_portraits[i], (16, 16))
            self.textbox.display_textbox()
        self.main_menu_running = False

    def show_start_screen(self):
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
            self.screen.blit(self.title, (0,0))
            pg.display.flip()
            
         
    def show_go_screen(self):
        # Maybe the confirmation to start game?
        pass

# create the game object
g = Game()

while g.main_menu_running:
    # mixer.init()
    # mixer.music.load('maps/MainMenuMusic.mp3')
    # mixer.music.play(-1) 
    g.show_start_screen() 
    while not g.main_menu_running:
        # mixer.music.stop()
        # mixer.music.load('maps/Town.mp3')
        # mixer.music.play(-1) 
        if g.loading_shop:
            g.new2()
            g.run()
        if g.loading_shop == False:
            g.new()
            g.run()
            g.show_go_screen()