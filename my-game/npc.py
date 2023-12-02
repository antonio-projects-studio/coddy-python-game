import pygame as pg
import math
from random import randint

class NPC():
    def __init__(self, game, pos):
        self.x, self.y = pos
        self.game = game
        # !В npc теперь через player получаем данные об игроке
        self.player = game.player
        self.theta = 0
    
    def draw(self):
        pg.draw.circle(self.game.screen, 'red',
                       (100 * self.x, 100 * self.y), 15)
        pg.draw.line(self.game.screen, 'red', (self.x * 100 + 14.5 * math.sin(self.theta), self.y * 100 - 14.5 * math.cos(self.theta)),
                     (self.x * 100 - 35 * math.cos(self.theta),
                     self.y * 100 - 35 * math.sin(self.theta)), 2)
        pg.draw.line(self.game.screen, 'red', (self.x * 100 - 14.5 * math.sin(self.theta), self.y * 100 + 14.5 * math.cos(self.theta)),
                     (self.x * 100 - 35 * math.cos(self.theta),
                     self.y * 100 - 35 * math.sin(self.theta)), 2)
    
    def look(self):
        dx = self.x - self.player.x
        dy = self.y - self.player.y
        self.dx, self.dy = dx, dy
        self.theta = math.atan2(dy, dx)

        delta = self.theta - self.player.angle
        if (dx > 0 and self.player.angle > math.pi) or (dx < 0 and dy < 0):
            delta += math.tau

        self.dist = math.hypot(dx, dy)
        self.norm_dist = self.dist * math.cos(delta)
        
        # !print(self.game.player.x)
        
    def run_logic(self):
        self.x += randint(20, 1000) / 10000
        self.y += randint(20, 1000) / 10000
        self.x -= randint(20, 1000) / 10000
        self.y -= randint(20, 1000) / 10000
    
    def update(self):
        self.look()
        self.run_logic()
    
    