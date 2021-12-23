import pygame as pg
import sys
import os
from settings import *
from characters import *
from shop import *
import pygame_menu
from textbox import*

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
        self.bg = pg.image.load(os.path.join(IMAGE_FOLDER, 'Background_Placeholder.png'))
        # Allow the user to hold the key down and it will auto repeat that key every .5 seconds
        pg.key.set_repeat(500, 100)
        self.loading = False # SHOP MAP TRANSITION
        if not self.loading: 
            self.load_map()
        self.main_running = True

    def load_map(self):
        # Grab map boundries from text file
        self.map_data = []
        with open(os.path.join(IMAGE_FOLDER, 'map.txt'), 'rt') as f:
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
                    NPC(self, col, row, OLD_MAN, OLD_MAN_PATH, OLD_MAN_TEXT, OLD_MAN_PORTRAIT, False)
                if tile == 'D':
                    NPC(self, col, row, BRONUT1, None, BRONUT_TEXT, BRONUT_PORTRAIT, True)
                          
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
        if self.loading:
            self.shop = Shop(self)
            self.shop.display_store()
            self.screen.blit(self.shop.bg, (0,0))
            self.player_sprite.draw(self.screen)
        else:    
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

    def start_game(self):
        self.main_menu.disable()
        self.clock.tick(200)
        self.screen.blit(BACKGROUND, (0,0))
        pg.display.update()
                     
        self.main_menu_conversations = ['But CJ, how can I fight without my stylish cardigan?', "Tony, it's not what is on the outside that counts. Besides, you're already plenty stylish!", "Yeah, Tony. We have to go and fight the yeti before he has a chance to attack the village.", "Let's check with that man over there. If he hasn't seen it then we'll just have to fight without it."]
        self.main_menu_portraits = [TONY, CJ, RYAN, JR]
        self.textbox = TextBox(self, None, None)
        for i in range(len((self.main_menu_conversations))):
            self.textbox.dialog_box.set_text(self.main_menu_conversations[i])
            self.textbox.dialog_box.set_portrait(self.main_menu_portraits[i], (16,16))
            self.textbox.display_textbox()
        self.main_running = False

    def show_start_screen(self):
        # Ryans sexy ass menu design
        self.main_menu_bg = pygame_menu.baseimage.BaseImage(image_path=os.path.join(IMAGE_FOLDER, 'title_placeholder.png'))
        self.menu_theme = pygame_menu.Theme(
            background_color=WHITE,
            title_background_color ='#08224f',
            title_font_color = WHITE,
            title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_ADAPTIVE)
        self.menu_theme.background_color = self.main_menu_bg
        self.main_menu = pygame_menu.Menu('RJCT Adventure', 800, 800, theme=self.menu_theme)
        self.main_menu.add.button('New Game', self.start_game, font_color=WHITE)
        self.main_menu.add.button('Load Game', self.start_game, font_color=WHITE)
        self.main_menu.add.button('Exit', self.start_game, font_color=WHITE)
        self.main_menu
        self.main_menu.mainloop(self.screen)
         

    def show_go_screen(self):
        # Maybe the confirmation to start game?
        pass

# create the game object
g = Game()

while g.main_running:
    g.show_start_screen() 
    while not g.main_running:
        g.new()
        g.run()
        g.show_go_screen()