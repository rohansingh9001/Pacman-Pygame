import pygame
import time

# initialise pygame
pygame.init()
tile_size = 8
sprite_size = 16

# The Map
# Key
# Wall - 1
# Path - 0

map_x = 8
map_y = 8
map = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],

]

# Title and Icon
pygame.display.set_caption("PacMan")
icon = pygame.image.load("pacman_open.png")
pygame.display.set_icon(icon)

# create the screen
screen = pygame.display.set_mode((tile_size*8, tile_size*8))

# Load images
wall_img = pygame.image.load('wall.png')
path_img = pygame.image.load('path.png')
player_img = pygame.image.load('pacman_open.png')
# Player's initial position in tiles
playerX = 0
playerY = 0


def player(x, y):
    screen.blit(player_img, (x*tile_size, y*tile_size))


def create_map(x, y, i):
    if i == 1:
        screen.blit(wall_img, (x*tile_size, y*tile_size))
    if i == 0:
        screen.blit(path_img, (x*tile_size, y*tile_size))

# Create the
# The wall class


class Wall():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.coordinate = (x, y)


class Path():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.coordinate = (x, y)


# Game Loop
running = True
while running:
    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for i in range(map_x):
        for j in range(map_y):
            create_map(i, j, map[j][i])
    player(1, 1)
    pygame.display.update()
    time.sleep(0.1)
