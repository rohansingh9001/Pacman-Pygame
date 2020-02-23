import pygame
import numpy as np
from mazegenerator import array
import math

wall_img = pygame.image.load('./assets/sprites/tiles/wall.png')

wall_1111 = pygame.image.load('./assets/sprites/tiles/wall_1111.png')
wall_1110 = pygame.image.load('./assets/sprites/tiles/wall_1110.png')
wall_1101 = pygame.image.load('./assets/sprites/tiles/wall_1101.png')
wall_1011 = pygame.image.load('./assets/sprites/tiles/wall_1011.png')
wall_0111 = pygame.image.load('./assets/sprites/tiles/wall_0111.png')
wall_1100 = pygame.image.load('./assets/sprites/tiles/wall_1100.png')
wall_1001 = pygame.image.load('./assets/sprites/tiles/wall_1001.png')
wall_0011 = pygame.image.load('./assets/sprites/tiles/wall_0011.png')
wall_0110 = pygame.image.load('./assets/sprites/tiles/wall_0110.png')
wall_1000 = pygame.image.load('./assets/sprites/tiles/wall_1000.png')
wall_0001 = pygame.image.load('./assets/sprites/tiles/wall_0001.png')
wall_0010 = pygame.image.load('./assets/sprites/tiles/wall_0010.png')
wall_0100 = pygame.image.load('./assets/sprites/tiles/wall_0100.png')
wall_1010 = pygame.image.load('./assets/sprites/tiles/wall_1010.png')
wall_0101 = pygame.image.load('./assets/sprites/tiles/wall_0101.png')

path_img = pygame.image.load('./assets/sprites/tiles/path.png')

pacman_l = pygame.image.load('./assets/sprites/pacman/pacman_l.png')
pacman_r = pygame.image.load('./assets/sprites/pacman/pacman_r.png')
pacman_u = pygame.image.load('./assets/sprites/pacman/pacman_u.png')
pacman_d = pygame.image.load('./assets/sprites/pacman/pacman_d.png')
pacman_c = pygame.image.load('./assets/sprites/pacman/pacman_c.png')

blinky_1_l = pygame.image.load('./assets/sprites/ghosts/blinky/blinky_1_l.png')
blinky_1_r = pygame.image.load('./assets/sprites/ghosts/blinky/blinky_1_r.png')
blinky_1_u = pygame.image.load('./assets/sprites/ghosts/blinky/blinky_1_u.png')
blinky_1_d = pygame.image.load('./assets/sprites/ghosts/blinky/blinky_1_d.png')
blinky_2_l = pygame.image.load('./assets/sprites/ghosts/blinky/blinky_2_l.png')
blinky_2_r = pygame.image.load('./assets/sprites/ghosts/blinky/blinky_2_r.png')
blinky_2_u = pygame.image.load('./assets/sprites/ghosts/blinky/blinky_2_u.png')
blinky_2_d = pygame.image.load('./assets/sprites/ghosts/blinky/blinky_2_d.png')

pinky_1_l = pygame.image.load('./assets/sprites/ghosts/pinky/pinky_1_l.png')
pinky_1_r = pygame.image.load('./assets/sprites/ghosts/pinky/pinky_1_r.png')
pinky_1_u = pygame.image.load('./assets/sprites/ghosts/pinky/pinky_1_u.png')
pinky_1_d = pygame.image.load('./assets/sprites/ghosts/pinky/pinky_1_d.png')
pinky_2_l = pygame.image.load('./assets/sprites/ghosts/pinky/pinky_2_l.png')
pinky_2_r = pygame.image.load('./assets/sprites/ghosts/pinky/pinky_2_r.png')
pinky_2_u = pygame.image.load('./assets/sprites/ghosts/pinky/pinky_2_u.png')
pinky_2_d = pygame.image.load('./assets/sprites/ghosts/pinky/pinky_2_d.png')

bashful_1_l = pygame.image.load(
    './assets/sprites/ghosts/bashful/bashful_1_l.png')
bashful_1_r = pygame.image.load(
    './assets/sprites/ghosts/bashful/bashful_1_r.png')
bashful_1_u = pygame.image.load(
    './assets/sprites/ghosts/bashful/bashful_1_u.png')
bashful_1_d = pygame.image.load(
    './assets/sprites/ghosts/bashful/bashful_1_d.png')
bashful_2_l = pygame.image.load(
    './assets/sprites/ghosts/bashful/bashful_2_l.png')
bashful_2_r = pygame.image.load(
    './assets/sprites/ghosts/bashful/bashful_2_r.png')
bashful_2_u = pygame.image.load(
    './assets/sprites/ghosts/bashful/bashful_2_u.png')
bashful_2_d = pygame.image.load(
    './assets/sprites/ghosts/bashful/bashful_2_d.png')

clyde_1_l = pygame.image.load('./assets/sprites/ghosts/clyde/clyde_1_l.png')
clyde_1_r = pygame.image.load('./assets/sprites/ghosts/clyde/clyde_1_r.png')
clyde_1_u = pygame.image.load('./assets/sprites/ghosts/clyde/clyde_1_u.png')
clyde_1_d = pygame.image.load('./assets/sprites/ghosts/clyde/clyde_1_d.png')
clyde_2_l = pygame.image.load('./assets/sprites/ghosts/clyde/clyde_2_l.png')
clyde_2_r = pygame.image.load('./assets/sprites/ghosts/clyde/clyde_2_r.png')
clyde_2_u = pygame.image.load('./assets/sprites/ghosts/clyde/clyde_2_u.png')
clyde_2_d = pygame.image.load('./assets/sprites/ghosts/clyde/clyde_2_d.png')

scared_1_b = pygame.image.load('./assets/sprites/ghosts/scared/scared_1_b.png')
scared_1_w = pygame.image.load('./assets/sprites/ghosts/scared/scared_1_w.png')
scared_1_b = pygame.image.load('./assets/sprites/ghosts/scared/scared_1_b.png')
scared_1_w = pygame.image.load('./assets/sprites/ghosts/scared/scared_1_w.png')

map_img = './assets/maps/original.png'
maze = np.array(array(map_img))

maze_x = len(maze[0])
maze_y = len(maze)

tile_size = 16  # 1 tile is 16x16 px
sprite_size = 16  # 1 sprite is 16x16 tile i.e. (16x16)x(16x16) px

# initialise pygame
pygame.init()

# Title and Icon
pygame.display.set_caption("PacMan")
icon = pygame.image.load("pacman_l.png")
pygame.display.set_icon(icon)

# create the screen
screen = pygame.display.set_mode((tile_size * maze_x, tile_size * maze_y))

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

def check_pos(coor1, coor2):
    x1, y1 = coor1
    x2, y2 = coor2
    return x1 == x2 and y1 == y2


def distance(cord1, cord2):
    i, j = cord1
    x, y = cord2
    return (((i-x)**2)+((j-y)**2))**(0.5)


def change_direction(direction):
    x, y = direction
    return (-1*x, -1*y)


def create_maze():
    # Code 1111: up, right, down, left
    for x in range(1, maze_x-1):
        for y in range(1, maze_y-1):
            # relative positions
            i = maze[y][x]
            u = maze[y-1][x]
            d = maze[y+1][x]
            l = maze[y][x-1]
            r = maze[y][x+1]
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


def get_threshold(inp):
    if inp > 200:
        return 0
    else:
        return math.floor(60*(math.exp(((-1)/200)*inp)))

def relu(coord):
    x,y = coord
    return (max(x,0),max(0,y))


   
