import pygame as pg
import pandas as pd
from settings import *
from random import randint, choice
import time
import sqlite3

class Battle():
    
    def __init__(self, game):
        # MUSIC AND SOUND SETTINGS
        # pg.mixer.init()
        # pg.mixer.music.load('maps/YetiBattle.mp3')
        # pg.mixer.music.play(-1)
        self.battle_theme = 'maps/YetiBattle.mp3'
        self.slash_sound = 'maps/slash.mp3'
        self.yeti_hit = 'maps/player_hit.wav'
        self.game = game
        self.connection = sqlite3.connect('db')
        self.turn = 1
        # Set up HP values(better in alt file)
        self.yeti_hp = 50
        self.jr_hp = 10
        self.cj_hp = 10
        self.ryan_hp = 10
        self.tony_hp = 10
        # Flag for showing blip
        self.battle_over = False
        self.update_time = pg.time.get_ticks()
        # Attack random character from list
        self.characters = ['cj', 'jr', 'ryan', 'tony']
        # Battle text settings
        self.attack_text = MAIN_FONT.render(str('ATTACK (A)'), True, (0, 0, 0))
        self.inventory_text = MAIN_FONT.render(str('INVENTORY (I)'), True, (0, 0, 0))
        self.defend_text = MAIN_FONT.render(str('DEFEND (D)'), True, (0, 0, 0))
        self.flee_text = MAIN_FONT.render(str('FLEE (F)'), True, (0, 0, 0))
        self.ryan_turn = MAIN_FONT.render(str('Ryan Turn'), True, (0, 0, 0))
        self.jr_turn = MAIN_FONT.render(str('Jr Turn'), True, (0, 0, 0))
        self.charlie_turn = MAIN_FONT.render(str('Charlie Turn'), True, (0, 0, 0))
        self.tony_turn = MAIN_FONT.render(str('Tony Turn'), True, (0, 0, 0))
        # Immediately jump intp battle upon initialization
        self.battle()

    def battle(self):
        while self.game.battling == True:
            df = pd.read_sql("SELECT * FROM health", self.connection)
            self.game.screen.blit(BATTLE_BG, (0,0))
            self.game.screen.blit(self.attack_text, (100,50))
            self.game.screen.blit(self.inventory_text, (200,50))
            self.game.screen.blit(self.defend_text, (100,75))
            self.game.screen.blit(self.flee_text, (200,75))

            # Ryan
            # ryan_hp = df[df['character'] == 'ryan']['hp'].values[0]
            ryan_hp_display = MAIN_FONT.render(str(self.ryan_hp), True, (0, 0, 0))
            ryan_total_hp = MAIN_FONT.render(str(' / 10'), True, (0, 0, 0)) # STRING
            if self.ryan_hp > 0:
                pg.draw.rect(self.game.screen,RED,(70,450,100,25))
                pg.draw.rect(self.game.screen,GREEN,(70,450,10*self.ryan_hp,25))
            else:
                pg.draw.rect(self.game.screen,RED,(250,450,100,25))
            self.game.screen.blit(ryan_hp_display, (90, 500))
            self.game.screen.blit(ryan_total_hp, (100, 500))
            
            if self.turn == 1 and self.ryan_hp > 0:
                self.game.screen.blit(self.ryan_turn, (65, 430))
            if self.turn == 2 and self.jr_hp > 0:
                self.game.screen.blit(self.jr_turn, (275, 400))
            if self.turn == 3 and self.cj_hp > 0:
                self.game.screen.blit(self.charlie_turn, (455, 400))
            if self.turn == 4 and self.tony_hp > 0:
                self.game.screen.blit(self.tony_turn, (660, 400))
            
            # Jr
            jr_hp_display = MAIN_FONT.render(str(self.jr_hp), True, (0, 0, 0))
            jr_total_hp = MAIN_FONT.render(str(' / 10'), True, (0, 0, 0))
            if self.jr_hp > 0:
                pg.draw.rect(self.game.screen,RED,(250,450,100,25))
                pg.draw.rect(self.game.screen,GREEN,(250,450,10*self.jr_hp,25))
            else:
                self.jr_hp = 0
                pg.draw.rect(self.game.screen,RED,(250,450,100,25))
            self.game.screen.blit(jr_hp_display, (290, 500))
            self.game.screen.blit(jr_total_hp, (300, 500))

            # CJ 
            cj_hp = df[df['character'] == 'cj']['hp'].values[0]
            cj_hp_display = MAIN_FONT.render(str(self.cj_hp), True, (0, 0, 0))
            cj_total_hp = MAIN_FONT.render(str(' / 10'), True, (0, 0, 0))
            if self.cj_hp > 0:
                pg.draw.rect(self.game.screen,RED,(450,450,100,25))
                pg.draw.rect(self.game.screen,GREEN,(450,450,10*self.cj_hp,25))
            else:
                self.cj_hp = 0
                pg.draw.rect(self.game.screen,RED,(450,450,100,25))
            self.game.screen.blit(cj_hp_display, (490, 500))
            self.game.screen.blit(cj_total_hp, (500, 500))

            # Tony
            tony_hp = df[df['character'] == 'tony']['hp'].values[0]
            tony_hp_display = MAIN_FONT.render(str(self.tony_hp), True, (0, 0, 0))
            tony_total_hp = MAIN_FONT.render(str(' / 10'), True, (0, 0, 0))
            if self.tony_hp > 0:
                pg.draw.rect(self.game.screen,RED,(650,450,100,25))
                pg.draw.rect(self.game.screen,GREEN,(650,450,10*self.tony_hp,25))
            else:
                self.tony_hp = 0
                pg.draw.rect(self.game.screen,RED,(250,450,100,25))
            self.game.screen.blit(tony_hp_display, (690, 500))
            self.game.screen.blit(tony_total_hp, (700, 500))

            # Yeti
            yeti_hp_display = MAIN_FONT.render(str(self.yeti_hp), True, (0, 0, 0))
            yeti_total_hp = MAIN_FONT.render(str(' / 50'), True, (0, 0, 0))
            pg.draw.rect(self.game.screen,RED,(175,120,500,25))
            pg.draw.rect(self.game.screen,GREEN,(175,120,10*self.yeti_hp,25))
            self.game.screen.blit(yeti_hp_display, (290, 200))
            self.game.screen.blit(yeti_total_hp, (300, 200))

            if self.yeti_hp <= 0:
                self.game.screen.blit(VICTORY_BG, (0,0))
                pg.mixer.stop()
                self.game.battling = False
                        
            pg.display.update()

            for event in pg.event.get():
                if self.turn == 1:
                    if self.ryan_hp > 0:
                        if event.type == pg.KEYDOWN:
                            if event.key == pg.K_a:
                                the_damage = randint(1,5)
                                self.yeti_hp = self.yeti_hp - the_damage
                                damage = MAIN_FONT.render('Ryan hit the yeti for ' + str(the_damage) + ' hp.', True, (0, 0, 0))
                                self.animate_hit()
                                self.game.screen.blit(damage, (500, 75))
                                # pg.display.flip()
                                pg.display.update()
                                time.sleep(1)
                                self.turn += 1
                                pg.event.wait()
                                break
                            if event.key == pg.K_f:
                                self.game.battling = False
                    else:
                        print('RYAN OUT')
                        self.turn += 1
                        pass
                  
                if self.turn == 2:
                    if self.jr_hp > 0:
                        if event.type == pg.KEYDOWN:
                            if event.key == pg.K_a:
                                the_damage = randint(1,5)
                                self.yeti_hp = self.yeti_hp - the_damage
                                damage = MAIN_FONT.render('Jr hit the yeti for ' + str(the_damage) + ' hp.', True, (0, 0, 0))
                                self.game.screen.blit(damage, (500, 75))
                                self.animate_hit()
                                # pg.display.flip()
                                pg.display.update()
                                time.sleep(1)
                                self.turn += 1
                                pg.event.wait()
                                break
                            if event.key == pg.K_f:
                                self.game.battling = False
                    else:
                        self.turn += 1
                        pass
                        
                if self.turn == 3:
                    if self.cj_hp > 0:
                        if event.type == pg.KEYDOWN:
                            if event.key == pg.K_a:
                                the_damage = randint(1,5)
                                self.yeti_hp = self.yeti_hp - the_damage
                                damage = MAIN_FONT.render('Charlie hit the yeti for ' + str(the_damage) + ' hp.', True, (0, 0, 0))
                                self.game.screen.blit(damage, (500, 75))
                                self.animate_hit()
                                # pg.display.flip()
                                pg.display.update()
                                time.sleep(1)
                                self.turn += 1
                                pg.event.wait()
                                break
                            if event.key == pg.K_f:
                                self.game.battling = False
                    else:
                        print('CJ OUT')
                        self.turn += 1
                        pass
              
                if self.turn == 4:
                    if self.tony_hp > 0:
                        if event.type == pg.KEYDOWN:
                            if event.key == pg.K_a:
                                the_damage = randint(1,5)
                                self.yeti_hp = self.yeti_hp - the_damage
                                damage = MAIN_FONT.render('Tony hit the yeti for ' + str(the_damage) + ' hp.', True, (0, 0, 0))
                                self.game.screen.blit(damage, (500, 75))
                                self.animate_hit()
                                # pg.display.flip()
                                pg.display.update()
                                time.sleep(1)
                                self.turn += 1
                                break
                            if event.key == pg.K_f:
                                self.game.battling = False
                    else:
                        print('TONY OUT')
                        self.turn += 1
                        pass     
                if self.turn == 5:
                    time.sleep(1)
                    the_damage = randint(5,10)
                    self.damaged_player = choice(self.characters)
                    if self.damaged_player == 'cj':
                        self.cj_hp = self.cj_hp - the_damage
                        if self.cj_hp <= 0:
                            self.characters.remove('cj')
                    if self.damaged_player == 'jr':
                        self.jr_hp = self.jr_hp - the_damage
                        if self.jr_hp <= 0:
                            self.characters.remove('jr')
                    if self.damaged_player == 'ryan':
                        self.ryan_hp = self.ryan_hp - the_damage
                        if self.ryan_hp <= 0:
                            self.characters.remove('ryan')
                    if self.damaged_player == 'tony':
                        self.tony_hp = self.tony_hp - the_damage
                        if self.tony_hp <= 0:
                            self.characters.remove('tony')
                    damage = MAIN_FONT.render(f'The yeti hit {self.damaged_player.title()} for ' + str(the_damage) + ' hp.', True, (0, 0, 0))
                    self.game.screen.blit(damage, (500, 75))
                    if self.yeti_hp > 0:
                        self.animate_yeti_hit()
                    pg.display.flip()
                    pg.display.update()
                    self.turn = 1
                    time.sleep(1)

    def animate_hit(self):
        # Slash images
        pg.mixer.music.load(self.slash_sound)
        pg.mixer.music.play(0)
        self.slash_images = [pg.image.load('maps/slash.png'), pg.image.load('maps/slash1.png'), pg.image.load('maps/slash2.png'), pg.image.load('maps/slash3.png'), pg.image.load('maps/slash4.png'), pg.image.load('maps/slash5.png')]
        index = 0
        image = self.slash_images[index]
        image = pg.transform.scale(image, (200,200))
        playing = True
        while playing:
            if index < len(self.slash_images):
                    self.game.screen.blit(image, (300,150))
                    pg.display.update()
                    index += 1
            else:
                playing = False
        # THIS WORKS BUT BLITS ALL SLASHES AT ONCE
        # for image in self.slash_images:
        #     pg.transform.scale(image, (200,200))
        #     self.game.screen.blit(image, (500,150))
    
    def animate_yeti_hit(self):
        pg.mixer.music.load(self.yeti_hit)
        pg.mixer.music.play(0)
        player_hit = pg.image.load('maps/take_damage.png')
        player_hit = pg.transform.scale(player_hit, (120,120))
        if self.damaged_player == 'ryan':
            self.game.screen.blit(player_hit, (75, 500))
        elif self.damaged_player == 'jr':
            self.game.screen.blit(player_hit, (270, 500))
        elif self.damaged_player == 'cj':
            self.game.screen.blit(player_hit, (455, 500))
        elif self.damaged_player == 'tony':
            self.game.screen.blit(player_hit, (615, 500))