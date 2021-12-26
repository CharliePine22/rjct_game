import sqlite3
import pygame as pg
import pandas as pd
from settings import *


class Inventory():
    def __init__(self, game):
        self.game = game
        self.inventory_open = True
        self.create_table()
        self.df = pd.read_sql("SELECT * FROM health", self.connection)
        self.display_inventory()
    
    def create_table(self):
        self.connection = sqlite3.connect('db')
        self.cursor = self.connection.cursor() 
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS health (character text, hp int)""")
        self.cursor.execute("INSERT INTO health VALUES (?,?)", ['ryan',5])
        self.cursor.execute("INSERT INTO health VALUES (?,?)", ['jr',10])
        self.cursor.execute("INSERT INTO health VALUES (?,?)", ['cj',10])
        self.cursor.execute("INSERT INTO health VALUES (?,?)", ['tony',10])
        self.connection.commit()
        self.cursor.close()
    
    def trigger_inventory(self):
        self.inventory_open = False
    
    def display_inventory(self):
        self.game.screen.blit(INVENTORY_PIC, (0,0))
        # Ryan
        ryan_hp = self.df[self.df['character'] == 'ryan']['hp'].values[0]
        ryan_hp_display = MAIN_FONT.render(str(ryan_hp), True, (0, 0, 0))
        ryan_total_hp = MAIN_FONT.render(str(' / 10'), True, (0, 0, 0))
        pg.draw.rect(self.game.screen,RED,(50,250,100,25))
        pg.draw.rect(self.game.screen,GREEN,(50,250,10*ryan_hp,25))
        self.game.screen.blit(ryan_hp_display, (90, 300))
        self.game.screen.blit(ryan_total_hp, (100, 300))
        # Jr
        jr_hp = self.df[self.df['character'] == 'jr']['hp'].values[0]
        jr_hp_display = MAIN_FONT.render(str(jr_hp), True, (0, 0, 0))
        jr_total_hp = MAIN_FONT.render(str(' / 10'), True, (0, 0, 0))
        pg.draw.rect(self.game.screen,RED,(250,250,100,25))
        pg.draw.rect(self.game.screen,GREEN,(250,250,10*jr_hp,25))
        self.game.screen.blit( jr_hp_display, (290, 300))
        self.game.screen.blit(jr_total_hp, (300, 300))

        # CJ 
        cj_hp = self.df[self.df['character'] == 'cj']['hp'].values[0]
        cj_hp_display = MAIN_FONT.render(str(cj_hp), True, (0, 0, 0))
        cj_total_hp = MAIN_FONT.render(str(' / 10'), True, (0, 0, 0))
        pg.draw.rect(self.game.screen,RED,(450,250,100,25))
        pg.draw.rect(self.game.screen,GREEN,(450,250,10*cj_hp,25))
        self.game.screen.blit(cj_hp_display, (490, 300))
        self.game.screen.blit(cj_total_hp, (500, 300))


        # Tony
        tony_hp = self.df[self.df['character'] == 'tony']['hp'].values[0]
        tony_hp_display = MAIN_FONT.render(str(tony_hp), True, (0, 0, 0))
        tony_total_hp = MAIN_FONT.render(str(' / 10'), True, (0, 0, 0))
        pg.draw.rect(self.game.screen,RED,(650,250,100,25))
        pg.draw.rect(self.game.screen,GREEN,(650,250,10*tony_hp,25))
        self.game.screen.blit(tony_hp_display, (690, 300))
        self.game.screen.blit(tony_total_hp, (700, 300))
        self.game.screen.blit(TONY_CARDIGAN, (65, 450))
        
        pg.display.update()
        while self.inventory_open == True:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_k:
                        print('HELLO')
                        self.trigger_inventory()
                                