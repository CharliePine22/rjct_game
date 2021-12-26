import pygame as pg
import pandas as pd
from settings import *
from random import randint, choice
import time
import sqlite3
from main import *

class Battle():
    
    def __init__(self, game):
        pg.mixer.init()
        pg.mixer.music.load('maps/YetiBattle.mp3')
        pg.mixer.music.play()
        self.game = game
        self.connection = sqlite3.connect('db')
        self.turn = 1
        self.yeti_hp = 50
        self.jr_hp = 10
        self.battle_over = False
        self.characters = ['cj', 'jr', 'ryan', 'tony']
        self.attack_text = MAIN_FONT.render(str('ATTACK (A)'), True, (0, 0, 0))
        self.inventory_text = MAIN_FONT.render(str('INVENTORY (I)'), True, (0, 0, 0))
        self.defend_text = MAIN_FONT.render(str('DEFEND (D)'), True, (0, 0, 0))
        self.flee_text = MAIN_FONT.render(str('FLEE (F)'), True, (0, 0, 0))
        self.ryan_turn = MAIN_FONT.render(str('Ryan Turn'), True, (0, 0, 0))
        self.jr_turn = MAIN_FONT.render(str('Jr Turn'), True, (0, 0, 0))
        self.charlie_turn = MAIN_FONT.render(str('Charlie Turn'), True, (0, 0, 0))
        self.tony_turn = MAIN_FONT.render(str('Tony Turn'), True, (0, 0, 0))
        self.battle()


    def battle(self):
        global jr_hp
        global yeti_hp
        while self.game.battling == True:
            df = pd.read_sql("SELECT * FROM health", self.connection)

            self.game.screen.blit(BATTLE_BG, (0,0))
            self.game.screen.blit(self.attack_text, (100,50))
            self.game.screen.blit(self.inventory_text, (200,50))
            self.game.screen.blit(self.defend_text, (100,75))
            self.game.screen.blit(self.flee_text, (200,75))

            # Ryan
            ryan_hp = df[df['character'] == 'ryan']['hp'].values[0]
            ryan_hp_display = MAIN_FONT.render(str(ryan_hp), True, (0, 0, 0))
            ryan_total_hp = MAIN_FONT.render(str(' / 10'), True, (0, 0, 0))
            pg.draw.rect(self.game.screen,RED,(50,450,100,25))
            pg.draw.rect(self.game.screen,GREEN,(50,450,10*ryan_hp,25))
            self.game.screen.blit(ryan_hp_display, (90, 500))
            self.game.screen.blit(ryan_total_hp, (100, 500))
            if self.turn == 1:
                self.game.screen.blit(self.ryan_turn, (100, 400))
            if self.turn == 2:
                self.game.screen.blit(self.jr_turn, (300, 400))
            if self.turn == 3:
                self.game.screen.blit(self.charlie_turn, (500, 400))
            if self.turn == 4:
                self.game.screen.blit(self.tony_turn, (700, 400))
            
            # Jr
            jr_hp_display = MAIN_FONT.render(str(self.jr_hp), True, (0, 0, 0))
            jr_total_hp = MAIN_FONT.render(str(' / 10'), True, (0, 0, 0))
            pg.draw.rect(self.game.screen,RED,(250,450,100,25))
            pg.draw.rect(self.game.screen,GREEN,(250,450,10*self.jr_hp,25))
            self.game.screen.blit( jr_hp_display, (290, 500))
            self.game.screen.blit(jr_total_hp, (300, 500))

            # CJ 
            cj_hp = df[df['character'] == 'cj']['hp'].values[0]
            cj_hp_display = MAIN_FONT.render(str(cj_hp), True, (0, 0, 0))
            cj_total_hp = MAIN_FONT.render(str(' / 10'), True, (0, 0, 0))
            pg.draw.rect(self.game.screen,RED,(450,450,100,25))
            pg.draw.rect(self.game.screen,GREEN,(450,450,10*cj_hp,25))
            self.game.screen.blit(cj_hp_display, (490, 500))
            self.game.screen.blit(cj_total_hp, (500, 500))

            # Tony
            tony_hp = df[df['character'] == 'tony']['hp'].values[0]
            tony_hp_display = MAIN_FONT.render(str(tony_hp), True, (0, 0, 0))
            tony_total_hp = MAIN_FONT.render(str(' / 10'), True, (0, 0, 0))
            pg.draw.rect(self.game.screen,RED,(650,450,100,25))
            pg.draw.rect(self.game.screen,GREEN,(650,450,10*tony_hp,25))
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
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_a:
                            the_damage = randint(20,50)
                            self.yeti_hp = self.yeti_hp - the_damage
                            damage = MAIN_FONT.render('Ryan hit the yeti for ' + str(the_damage) + ' hp.', True, (0, 0, 0))
                            # background.blit(damage, (500, 75))
                            self.game.screen.blit(damage, (500, 75))
                            pg.display.flip()
                            pg.display.update()
                            time.sleep(1)
                            self.turn += 1
                            pg.event.wait()
                            break
                        if event.key == pg.K_f:
                            self.game.battling = False
                            
                if self.turn == 2:
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_a:
                            the_damage = randint(20,50)
                            self.yeti_hp = self.yeti_hp - the_damage
                            damage = MAIN_FONT.render('Jr hit the yeti for ' + str(the_damage) + ' hp.', True, (0, 0, 0))
                            # background.blit(damage, (500, 75))
                            self.game.screen.blit(damage, (500, 75))
                            pg.display.flip()
                            pg.display.update()
                            time.sleep(1)
                            self.turn += 1
                            pg.event.wait()
                            break
                if self.turn == 3:
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_a:
                            the_damage = randint(15,555)
                            self.yeti_hp = self.yeti_hp - the_damage
                            damage = MAIN_FONT.render('Charlie hit the yeti for ' + str(the_damage) + ' hp.', True, (0, 0, 0))
                            # background.blit(damage, (500, 75))
                            self.game.screen.blit(damage, (500, 75))
                            pg.display.flip()
                            pg.display.update()
                            time.sleep(1)
                            self.turn += 1
                            pg.event.wait()
                            break
                        
                if self.turn == 4:
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_a:
                            the_damage = randint(1,5)
                            self.yeti_hp = self.yeti_hp - the_damage
                            damage = MAIN_FONT.render('Tony hit the yeti for ' + str(the_damage) + ' hp.', True, (0, 0, 0))
                            # background.blit(damage, (500, 75))
                            self.game.screen.blit(damage, (500, 75))
                            pg.display.flip()
                            pg.display.update()
                            time.sleep(1)
                            self.turn += 1
                            break
                        
                if self.turn == 5:
                    time.sleep(1)
                    the_damage = randint(1,5)
                    self.jr_hp = self.jr_hp - the_damage
                    damage = MAIN_FONT.render('The yeti hit Jr for ' + str(the_damage) + ' hp.', True, (0, 0, 0))
                    # background.blit(damage, (500, 75))
                    self.game.screen.blit(damage, (500, 75))
                    pg.display.flip()
                    pg.display.update()
                    self.turn = 1
                    time.sleep(1)
