import pygame as pg
import sys
from settings import *
from map import *
from player import *
#! Импорт всего что в npc
from npc import *
# from player import *
# from raycasting import *
# from npc_control import *
# from pathfinding import *
# from finish import *
# from textures import *
# from sound import *


class Game:
    def __init__(self) -> None:
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.level = 1
        self.new_game()
        # self.sounds = Sound(self)
        # pg.mixer.music.play(-1)

    def new_game(self):
        self.delta_time = self.clock.tick(FPS)
        # self.raycasting = RayCasting(self)
        self.map = Map(self)
        self.player = Player(game=self)
        #! Добавляем копию npc
        self.npc = NPC(game=self, pos=(5, 5))
        self.npc2 = NPC(game=self, pos=(6, 6))
        # self.textures = Textures(self)
        # self.npc_control = NpcControl(self)
        # self.finish = Finish(self)
        # self.pathfinding = PathFinding(self)

    def update(self):
        # self.raycasting.update()
        pg.display.flip()
        self.player.update()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.0f} danya_lox')
        # self.finish.update()
        # !Запустили update npc (look)
        self.npc.update()
        self.npc2.update()

    def draw(self):
        self.screen.fill('black')
        self.map.draw()
        self.player.draw()
        #! Не забыть отрисовку
        self.npc.draw()
        self.npc2.draw()
        #self.player.draw()
        # self.npc_control.update()
        # self.finish.draw()

    def check_event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def run(self):
        while True:
            self.check_event()
            self.draw()
            self.update()


if __name__ == '__main__':
    game = Game()
    game.run()

