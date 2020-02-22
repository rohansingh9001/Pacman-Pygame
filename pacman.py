'''
Refrences - 
    1. https://www.gamasutra.com/view/feature/132330/the_pacman_dossier.php?page=1
    2. https://gameinternals.com/understanding-pac-man-ghost-behavior

This is an attempt to recreate pacman in pygame.
AUTHORS - 
    1. Rohan Singh 
    2. Maruf Hussain
    3. Tarun Singh Tomar

This version of pacman will be used to implement
a genetic algori 
'''


import pygame
import time
from mazegenerator import array

# initialise pygame
pygame.init()
tile_size = 16  # 1 tile is 16x16 px
sprite_size = 16  # 1 sprite is 16x16 tile i.e. (16x16)x(16x16) px

# The Map
# Key
# Wall - 1
# Path - 0

# The map img name
map_img = 'Maze.png'

map = array(map_img)
map_x = len(map[0])
map_y = len(map)


# Create a tuple addition function which returns the direction.


def get_block(current, direction):
    curr_x, curr_y = current
    dir_x, dir_y = direction

    return (curr_x + dir_x, curr_y + dir_y)


# Create a function to convert the coordinates to px
def coor_to_px(coordinates):
    x, y = coordinates
    return (x * tile_size, y * tile_size)


# Check if two entities are on the same tile.

def check_pos(ent1, ent2):
    pass


# Title and Icon
pygame.display.set_caption("PacMan")
icon = pygame.image.load("pacman_open.png")
pygame.display.set_icon(icon)

# create the screen
screen = pygame.display.set_mode((tile_size * map_x, tile_size * map_y))

# Load images
wall_img = pygame.image.load('wall.png')
wall_1111 = pygame.image.load('Wall_1111.png')
wall_1110 = pygame.image.load('Wall_1110.png')
wall_1101 = pygame.image.load('Wall_1101.png')
wall_1011 = pygame.image.load('Wall_1011.png')
wall_0111 = pygame.image.load('Wall_0111.png')
wall_1100 = pygame.image.load('Wall_1100.png')
wall_1001 = pygame.image.load('Wall_1001.png')
wall_0011 = pygame.image.load('Wall_0011.png')
wall_0110 = pygame.image.load('Wall_0110.png')
wall_1000 = pygame.image.load('Wall_1000.png')
wall_0001 = pygame.image.load('Wall_0001.png')
wall_0010 = pygame.image.load('Wall_0010.png')
wall_0100 = pygame.image.load('Wall_0100.png')
wall_1010 = pygame.image.load('Wall_1010.png')
wall_0101 = pygame.image.load('Wall_0101.png')
path_img = pygame.image.load('path.png')
player_img = pygame.image.load('pacman_open.png')
# Player's initial position in tiles
playerX = 0
playerY = 0
playerMove = 1

def create_map():
    # Code 1111: up, right, down, left
    for x in range(1, map_x-1):
        for y in range(1, map_y-1):

            i = map[y][x]
            u = map[y-1][x]
            d = map[y+1][x]
            l = map[y][x-1]
            r = map[y][x+1]
            if i == 0:
                screen.blit(path_img, coor_to_px((x, y)))
            if i == 1:
                if u == 1 and d == 1 and r == 1 and l == 1:
                    screen.blit(wall_img, coor_to_px((x, y)))

                if u == 0 and d == 1 and r == 1 and l == 1:
                    screen.blit(wall_1000, coor_to_px((x, y)))
                if u == 1 and d == 0 and r == 1 and l == 1:
                    screen.blit(wall_0010, coor_to_px((x, y)))
                if u == 1 and d == 1 and r == 0 and l == 1:
                    screen.blit(wall_0100, coor_to_px((x, y)))
                if u == 1 and d == 1 and r == 1 and l == 0:
                    screen.blit(wall_0001, coor_to_px((x, y)))

                if u == 0 and d == 0 and r == 1 and l == 1:
                    screen.blit(wall_1010, coor_to_px((x, y)))
                if u == 1 and d == 0 and r == 0 and l == 1:
                    screen.blit(wall_0110, coor_to_px((x, y)))
                if u == 1 and d == 1 and r == 0 and l == 0:
                    screen.blit(wall_0101, coor_to_px((x, y)))
                if u == 0 and d == 1 and r == 1 and l == 0:
                    screen.blit(wall_1001, coor_to_px((x, y)))
                if u == 1 and d == 0 and r == 1 and l == 0:
                    screen.blit(wall_0011, coor_to_px((x, y)))
                if u == 0 and d == 1 and r == 0 and l == 1:
                    screen.blit(wall_1100, coor_to_px((x, y)))

                if u == 1 and d == 0 and r == 0 and l == 0:
                    screen.blit(wall_0111, coor_to_px((x, y)))
                if u == 0 and d == 1 and r == 0 and l == 0:
                    screen.blit(wall_1101, coor_to_px((x, y)))
                if u == 0 and d == 0 and r == 1 and l == 0:
                    screen.blit(wall_1011, coor_to_px((x, y)))
                if u == 0 and d == 0 and r == 0 and l == 1:
                    screen.blit(wall_1110, coor_to_px((x, y)))


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


class Pacman():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.coordinate = (x, y)
        self.prev = None
        self.direction = (1, 0)
        self.next = get_block(self.coordinate, self.direction)

    # The player placement function

    def place(self):
        screen.blit(player_img, coor_to_px(self.coordinate))


# Create a walls list
walls = []

# Create a path list
paths = []


# Game Loop
running = True

# Initialise characters
pacman = Pacman(2, 2)

while running:
    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                pacman.direction = (1,0)
    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pacman.direction = (-1,0)
    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pacman.direction = (0,-1)
    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                pacman.direction = (0,1)                                                   

    if event.type == pygame.KEYUP:
        playerMove = 0                           

    create_map()
    pacman.prev = pacman.coordinate
    pacman.coordinate = get_block(pacman.coordinate,pacman.direction)
    pacman.place()
    pygame.display.update()
    time.sleep(0.1)
