import pygame as pg
from player import Player
from world import World, Wall
from enemy import Enemy
from camera import Camera
import constant as c
from os import path

def load_map_data(group):
    game_folder = path.dirname(__file__)
    world_data = World(path.join(game_folder, 'map.txt'))

    for row, tiles in enumerate(world_data.data):
        for col, tile in enumerate(tiles):
            if tile == '1':
                wall = Wall(col, row, group)
                wall_group.add(wall)
            if tile == 'p':
                player = Player(col, row, group)
                player_group.add(player)
            if tile == 'e':
                enemy = Enemy(col, row, group)
                enemy_group.add(enemy)
    return world_data, player


# inititialise pygame
pg.init()

# create clock
clock = pg.time.Clock()

# create game window
screen = pg.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
pg.display.set_caption(c.window_name)

# load images
# player_image = pg.image.load().convert_alpha()

wall_group = pg.sprite.Group()
player_group = pg.sprite.Group()
enemy_group = pg.sprite.Group()
all_groups = Camera()

# load map data
world_data, player = load_map_data(all_groups)

# game loop
run = True
while run:
    clock.tick(c.FPS)

    screen.fill(c.darkGray)

    all_groups.custom_draw(player)

    # pg.draw.lines(screen, "grey0", False, waypoints)

    # update groups
    all_groups.update(wall_group)

    # even handler
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    # update display
    pg.display.flip()

pg.quit()





