from setting import *
import pygame as pg
import math

class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE
    
    def movement(self):
        # Toán (Tại sao lập trình lại có toán chứ :v )
        sin_a = math.sin(self.angle) # sin dùng cho đi thẳng
        cos_a = math.cos(self.angle) # cos dùng cho đi ngang
        dx, dy = 0, 0
        speed = PLAYER_SPEED * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        # Nút bấm
        keys = pg.key.get_pressed()
        if keys[pg.K_w]: # Nhấn W (K_w)
            dx += speed_cos
            dy += speed_sin

        if keys[pg.K_s]: # Nhấn S (K_s)
            dx += -speed_cos
            dy += -speed_sin
        
        if keys[pg.K_a]: # Nhấn A (K_a)
            dx += speed_sin
            dy += -speed_cos

        if keys[pg.K_d]: # Nhấn D (K_d)
            dx += -speed_sin
            dy += speed_cos

        self.check_wall_collision(dx, dy)
        
        if keys[pg.K_LEFT]:
            self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        if keys[pg.K_RIGHT]:
            self.angle += PLAYER_ROT_SPEED * self.game.delta_time
        self.angle %= math.tau # tau = 2*pi

    def check_wall(self, x, y):
        return(x, y) not in self.game.map.world_map
    
    def check_wall_collision(self, dx, dy):
        if self.check_wall(int(self.x + dx), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy)):
            self.y += dy

    def draw(self):
        pg.draw.line(surface = self.game.screen, 
                    color = 'yellow', 
                    start_pos = (self.x * 100, self.y * 100),
                    end_pos = (self.x * 100 + WIDTH * math.cos(self.angle),self.y * 100 + WIDTH * math.sin(self.angle)),
                    width = 2)
        
        pg.draw.circle(surface = self.game.screen,
                       color = 'green',
                       center = (self.x * 100, self.y * 100),
                       radius = 15)
        
    def update(self):
        self.movement()
    
    @property
    def pos(self):
        return self.x, self.y
    
    @property
    def map_pos(self):
        return int(self.x), int(self.y)
    
