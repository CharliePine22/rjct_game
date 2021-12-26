import pygame as pg
import os 
from settings import *
from textbox import *
from shop import *

vec = pg.math.Vector2

def collide_with_wall(sprite, group, dir):
        # dir == direction (x or y)
        if dir == 'x':
            # List of colli
            hits = pg.sprite.spritecollide(sprite, group, False)
            if hits:
                # If we were moving right and run into a wall
                if sprite.vx > 0:
                    # The wall we hit - the width of the sprite
                    sprite.x = hits[0].rect.left - sprite.rect.width
                # Moving left and run into wall
                if sprite.vx < 0:
                    sprite.x = hits[0].rect.right 
                # Reduce speed to 0 and place rect at new position
                sprite.vx = 0
                sprite.rect.x = sprite.x
        if dir == 'y':
            hits = pg.sprite.spritecollide(sprite, group, False)
            if hits:
                # Moving up and run into a wall
                if sprite.vy > 0:
                    sprite.y = hits[0].rect.top - sprite.rect.height
                # Moving down and run into a wall 
                if sprite.vy < 0:
                    sprite.y = hits[0].rect.bottom
                sprite.vy = 0
                sprite.rect.y = sprite.y

                
#################################### PLAYER CLASS ################################################## 
class Player(pg.sprite.Sprite):
    # Sprite for player using Pygames sprite object
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.player_sprite
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        # Image for what the sprite looks like
        self.image = pg.image.load(os.path.join(IMAGE_FOLDER, "RJCT_TONY.png")).convert()
        self.image = pg.transform.scale(self.image, (35, 35))
        # Colorkey tells pygame to ignore a certain color so the background of sprite is transparent
        self.image.set_colorkey(YELLOW)
        # Rect is a pygame rectangle that encloses the sprite(useful for collisions, movement, etc.)
        self.rect = self.image.get_rect()
        # Used for spawning in on the map
        self.x = x * TILESIZE
        self.y = y * TILESIZE

    def get_keys(self):
        # Give player velocity for smoother movement
        self.vx, self.vy = 0, 0
        # Check what keys are currently being held down
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.vx = -PLAYER_SPEED
        if keys[pg.K_RIGHT]:
            self.vx = PLAYER_SPEED
        if keys[pg.K_UP]:
            self.vy = -PLAYER_SPEED
        if keys[pg.K_DOWN]:
            self.vy = PLAYER_SPEED
        if self.x > 195 and self.x < 211 and self.y == 576 and keys[pg.K_RETURN]:
                self.game.loading = True
        if self.x > 370 and self.x < 430 and self.y < 110 and keys[pg.K_RETURN]:
                self.game.battling = True

        
        # Reduces speed for diagnally moving
        if self.vx != 0 and self.vy != 0:
            self.vx *= 0.7071
            self.vy *= 0.7071

    def move(self, dx=0, dy=0):
        # Move the x and y coordinates by however much the distance to dx and dy coordinates is
        if not self.collide_with_wall(dx,dy):
            self.x += dx
            self.y += dy
        
    def update(self):
        hits = pg.sprite.spritecollide(self, self.game.npcs, False)
        if hits:
            # walking right
            if self.vx > 0:
                self.x = hits[0].rect.left - self.rect.width
                self.vx = 0
                self.rect.x = self.x
            # walking left
            if self.vx < 0:
                self.x = hits[0].rect.right
                self.vx = 0
                self.rect.x = self.x
            # walking down
            if self.vy > 0:
                self.y = hits[0].rect.top - self.rect.height
                self.vy = 0
                self.rect.y = self.y
            # walking up
            if self.vy < 0:
                self.y = hits[0].rect.bottom
                self.vy = 0
                self.rect.y = self.y
                
        self.get_keys()
        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt
        self.rect.x = self.x
        collide_with_wall(self, self.game.walls, 'x')
        self.rect.y = self.y
        collide_with_wall(self, self.game.walls, 'y')
      
#################################### NPC CLASS ##################################################   
class NPC(pg.sprite.Sprite):
    def __init__(self, game, x, y, image, waypoints, text, portrait, animate):
        self.groups = game.all_sprites, game.npcs
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        # NPC Settings
        self.image = image
        self.animate = animate
        self.update_time = pg.time.get_ticks()
        self.image.set_colorkey(BLACK)
        self.text = text
        # For animation iteration
        self.animations = [BRONUT1, BRONUT2]
        self.index = 0
        # NPC Positioning
        self.pos = vec(x, y) * TILESIZE        
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.max_speed = 3
        # NPC Speed, Position, and Acceleration
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.portrait = portrait
        self.textbox = TextBox(self.game, self.text, self.portrait)
        # NPC Path Creation 
        self.waypoints = waypoints
        # For looping to next target destination
        if self.waypoints != None:
            self.waypoint_index = 0
            self.target = self.waypoints[self.waypoint_index]
            self.target_radius = 50
        # If animate is true, set image to first frame
        if self.animate:
            self.image = self.animations[self.index]
    
    def update(self):
        # If the NPC animation flag is True
        if self.animate:
            animation_cooldown = 200
            self.image = self.animations[self.index]
            # If the time since starting is larger than the cooldown, go to the next frame
            if pg.time.get_ticks() - self.update_time > animation_cooldown:
                # Reset update time to current time to keep running loop
                self.update_time = pg.time.get_ticks()
                self.index += 1
            # If there are no images/frames left, reset index to 0
            if self.index >= len(self.animations):
                self.index = 0
    
        # If the NPC collides with the player sprite
        hits = pg.sprite.spritecollide(self, self.game.player_sprite, False)
        if hits:
            self.textbox.display_textbox()
        if self.waypoints != None:
            heading = self.target - self.pos
            distance = heading.length()  # Distance to the target.
            # Allows the NPC to slow down towards endpoint or else he flies off the screen
            heading.normalize_ip()
            if distance <= 2:  # We're closer than 2 pixels.
                # The modulo sets the index back to 0 if it's equal to the length.
                self.waypoint_index = (self.waypoint_index + 1) % len(self.waypoints)
                self.target = self.waypoints[self.waypoint_index]
            if distance <= self.target_radius:
                # If we're approaching the target, we slow down.
                self.vel = heading * (distance / self.target_radius * self.max_speed)
            else:  # Otherwise move with max_speed.
                self.vel = heading * self.max_speed
            self.pos += self.vel
            self.rect.center = self.pos       
        
#################################### WALL CLASS ##################################################
class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE