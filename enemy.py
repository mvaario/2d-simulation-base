import pygame as pg
import constant as c
from pygame.math import Vector2


class Enemy(pg.sprite.Sprite):
    def __init__(self, pos_x, pos_y, group):
        super().__init__(group)
        self.original_image = pg.Surface((c.tilesize * 2, c.tilesize * 2), pg.SRCALPHA)
        self.original_image.fill((0,0,0))
        self.original_image.set_colorkey((0, 0, 0))

        self.vel = 0
        self.angle_vel = 0
        self.angle = 0
        self.dir = [0, 0]

        self.image = self.original_image
        pg.draw.circle(self.image, c.red, (c.tilesize, c.tilesize), c.tilesize)
        self.image.set_alpha(255)
        self.rect = self.image.get_rect()

        self.pos = [pos_x * c.tilesize + c.tilesize / 2, pos_y * c.tilesize + c.tilesize / 2]
        self.rect.center = self.pos

    def move(self, wall_group):
        if self.angle > 90:
            angle = 180 - self.angle
        elif self.angle < -90:
            angle = (180 + self.angle) * -1
        else:
            angle = self.angle
        x = (angle / 90) * -1

        angle = self.angle
        if angle == 0:
            angle = -90
        elif angle == 180 or angle == -180:
            angle = 90
        elif angle > 0:
            angle -= 90
        elif angle < 0:
            angle += 90
            angle = -angle

        y = angle / 90

        # normalizes multipliers
        self.dir = Vector2(x, y)
        self.dir = self.dir.normalize()

        # move and check collisions with walls
        self.pos[0] = self.pos[0] + self.dir[0] * self.vel
        self.rect.center = self.pos
        self.collide_with_walls(wall_group, 'x')

        self.pos[1] = self.pos[1] + self.dir[1] * self.vel
        self.rect.center = self.pos
        self.collide_with_walls(wall_group, 'y')

    def target(self):
        pass

    def update(self, wall_group):
        # get target
        self.target()


        # rotate
        self.rotate()

        # move player
        self.move(wall_group)

    def collide_with_walls(self, wall_group, direction):
        hits = pg.sprite.spritecollide(self, wall_group, False)
        if hits:
            if direction == 'x':
                self.pos[0] = self.pos[0] - self.dir[0] * self.vel
                self.rect.center = self.pos
            if direction == 'y':
                self.pos[1] = self.pos[1] - self.dir[1] * self.vel
                self.rect.center = self.pos

    def rotate(self):
        self.angle += self.angle_vel
        # self.angle = round(self.angle)
        if self.angle > 180:
            self.angle -= 360
        elif self.angle <= -180:
            self.angle += 360