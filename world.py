import pygame as pg
import constant as c

class World:
    def __init__(self, file_name):
        self.data = []
        with open(file_name, 'rt') as f:
            for line in f:
                self.data.append(line.strip())

        self.tile_width = len(self.data[0])
        self.tile_height = len(self.data)

class Wall(pg.sprite.Sprite):
    def __init__(self, pos_x, pos_y, group):
        super().__init__(group)
        self.image = pg.Surface((c.tilesize, c.tilesize))
        self.image.fill(c.orange)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x * c.tilesize
        self.rect.y = pos_y * c.tilesize


