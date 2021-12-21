import pygame as pg
import textboxify
from settings import *

class TextBox(pg.sprite.LayeredDirty):
    def __init__(self, game, text, image):
        pg.sprite.LayeredDirty.__init__(self)
        self.game = game
        self.image = image
        self.dialog_box = textboxify.TextBoxFrame(
                text= text,
                text_width=600,
                lines=5,
                pos=(0, 0),
                padding=(120, 50),
                font_color=WHITE,
                font_size=26,
                bg_color=(8, 34, 79)
        )
        self.dialog_box.set_portrait(image, size=(16, 16))
        self.conversation = [self.dialog_box]
        
    def display_textbox(self):
        # Add and update textbox
        while self.dialog_box.words:
            self.add(self.conversation[0])
            self.update()
            current_dialog = self.draw(self.game.screen)
            pg.display.update(current_dialog)
        self.wait_for_confirm()
    
    def wait_for_confirm(self):
        # Stop everything until the textbox is done rendering or user quits
        pg.event.wait()
        waiting = True
        while waiting:
            self.game.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    # Escape closes box regardless of text being complete or not
                    if event.key == pg.K_ESCAPE:
                        waiting = False
                    if event.key == pg.K_RETURN:
                        self.dialog_box.reset(hard=True)
                        self.dialog_box.set_text('Good luck!')
                        waiting = False
                        