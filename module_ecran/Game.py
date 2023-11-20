import pygame as pg
from data import *


class Game:
    def __init__(self):
        pg.display.init()
        self.window = pg.display.set_mode()
        self.width = self.window.get_width()
        self.height = self.window.get_height()
        self.running = True
        self.update = True
        self.clock = pg.time.Clock()
        self.zoom = 1
        self.square = [200, 200]
        pg.display.toggle_fullscreen()

    def quit(self):
        print(self.width, self.height)
        pg.display.quit()

    def draw(self):
        self.window.fill(pg.Color(BLACK))
        pg.draw.rect(self.window, pg.Color(RED), pg.Rect(
            self.width // 2,  self.height // 2, self.square[0], self.square[1]))
        pg.display.update()
        self.update = False

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_q or event.key == pg.K_ESCAPE:
                    self.running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 4:
                    self.zoom += 0.1
                    self.update = True
                elif event.button == 5:
                    self.zoom -= 0.1
                    self.update = True

    def loop(self):
        while (self.running):
            self.clock.tick(FPS)
            self.check_events()
            if self.update:
                self.draw()
                print(self.zoom)

        self.quit()
