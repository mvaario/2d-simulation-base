import pygame as pg
import constant as c

class Camera(pg.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pg.display.get_surface()

        # camera offset
        self.offset = pg.math.Vector2()
        self.half_w = self.display_surface.get_size()[0] / 2
        self.half_h = self.display_surface.get_size()[1] / 2

    def draw_grid(self):
        for x in range(0, c.SCREEN_WIDTH, c.tilesize*2):
            pg.draw.line(self.display_surface, c.lightGray, (x, 0), (x, c.SCREEN_HEIGHT))
        for y in range(0, c.SCREEN_HEIGHT, c.tilesize*2):
            pg.draw.line(self.display_surface, c.lightGray, (0, y), (c.SCREEN_WIDTH, y))

    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - self.half_w
        self.offset.y = player.rect.centery - self.half_h

        # ground
        self.draw_grid()

        # short sprites with y-axis
        for sprite in sorted(self.sprites(), key=lambda sprite:sprite.rect.centery):
            offset_position = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_position)