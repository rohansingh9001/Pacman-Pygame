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
a genetic algorithm which will be able to play
pacman.

A project by Robotics Club IIT Jodhpur.

'''

__version__ = '0.16'


import pygame
import time
from utils import *

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
        self.direction = (1, 0)
        self.next = get_block(self.coordinate, self.direction)
        self.sprite = pacman_l
        self.mouth_open = False

    # Make a function to update pacman

    def update(self):

        # Pacman Sprite Update
        if self.mouth_open:
            self.sprite = pacman_c
        else:
            if self.direction == (1, 0):
                self.sprite = pacman_l
            if self.direction == (-1, 0):
                self.sprite = pacman_r
            if self.direction == (0, 1):
                self.sprite = pacman_d
            if self.direction == (0, -1):
                self.sprite = pacman_u
        self.mouth_open = ~(self.mouth_open)

        i, j = self.next
        if maze[j][i] == 0:
            self.coordinate = get_block(self.coordinate, self.direction)

        self.next = get_block(self.coordinate, self.direction)
        # screen.blit(self.sprite, coor_to_px(self.coordinate))

    def draw(self):
        screen.blit(self.sprite, coor_to_px(self.coordinate))


class Ghost():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.coordinate = (x, y)  # (29,27) by default
        self.left = None
        self.right = None
        self.direction = (0, 1)
        self.target = pacman.coordinate
        self.sprite = blinky_1_l
        self.phase_1 = False
        self.mode = "chase"
        self.home = (2, 3)

    def draw(self):
        screen.blit(self.sprite, coor_to_px(self.coordinate))

    def getpos(self):
        x, y = self.direction
        self.left = (y, x)
        self.right = (-1*y, -1*x)

    def type_node(self):
        poss = []
        i, j = get_block(self.coordinate, self.direction)
        if maze[j][i] == 0:
            poss.append(self.direction)
        i, j = get_block(self.coordinate, self.left)
        if maze[j][i] == 0:
            poss.append(self.left)
        i, j = get_block(self.coordinate, self.right)
        if maze[j][i] == 0:
            poss.append(self.right)
        # print(poss)
        return poss

    def update(self):
        # Pacman Sprite Update
        if self.phase_1:
            if self.direction == (1, 0):
                self.sprite = blinky_1_r
            if self.direction == (-1, 0):
                self.sprite = blinky_1_l
            if self.direction == (0, 1):
                self.sprite = blinky_1_d
            if self.direction == (0, -1):
                self.sprite = blinky_1_u
        else:
            if self.direction == (1, 0):
                self.sprite = blinky_2_r
            if self.direction == (-1, 0):
                self.sprite = blinky_2_l
            if self.direction == (0, 1):
                self.sprite = blinky_2_d
            if self.direction == (0, -1):
                self.sprite = blinky_2_u
        self.phase_1 = ~(self.phase_1)

        self.getpos()
        poss = self.type_node()
        if(len(poss) == 1):
            self.coordinate = get_block(self.coordinate, poss[0])
            self.direction = poss[0]
        elif (len(poss) >= 2):
            dist = 100000000
            for pos in poss:
                if dist > distance(get_block(self.coordinate, pos), self.target):
                    dist = distance(
                        get_block(self.coordinate, pos), self.target)
                    self.direction = pos
            self.coordinate = get_block(self.coordinate, self.direction)
        # else:
        #     a, b = self.direction
        #     self.direction = (-a, -b)


# Game Loop
running = True

# Initialise characters
pacman = Pacman(13, 19)
pac_upd = 0
ghost1 = Ghost(13, 11)
ghost2 = Ghost(13, 7)
ghost3 = Ghost(3, 22)
ghost4 = Ghost(23, 22)

entities = [pacman, ghost1, ghost2, ghost3, ghost4]

while running:

    if pacman.coordinate == ghost1.coordinate or pacman.coordinate == ghost2.coordinate or pacman.coordinate == ghost3.coordinate or pacman.coordinate == ghost4.coordinate:
        break

    for ghost in entities[1:]:
        if ghost.target == ghost.coordinate:
            ghost.target = pacman.coordinate

    for entity in entities:
        if entity.coordinate == (23,13):
            entity.coordinate = (4,13)
        elif entity.coordinate == (3,13):
            entity.coordinate = (22,13)    

    print(pacman.coordinate)
    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if event.type == pygame.KEYDOWN:

        if event.key == pygame.K_RIGHT:
            i, j = pacman.coordinate
            i += 1
            if maze[j][i] == 0:
                pacman.direction = (1, 0)

        if event.key == pygame.K_LEFT:
            i, j = pacman.coordinate
            i -= 1
            if maze[j][i] == 0:
                pacman.direction = (-1, 0)

        if event.key == pygame.K_UP:
            i, j = pacman.coordinate
            j -= 1
            if maze[j][i] == 0:
                pacman.direction = (0, -1)

        if event.key == pygame.K_DOWN:
            i, j = pacman.coordinate
            j += 1
            if maze[j][i] == 0:
                pacman.direction = (0, 1)

    if event.type == pygame.KEYUP:
        playerMove = 0

    create_maze()

    if pac_upd == 5:
        pacman.update()
        ghost1.update()
        ghost2.update()
        ghost3.update()
        ghost4.update()
        pac_upd = 0

    pac_upd += 1
    pacman.draw()
    ghost1.draw()
    ghost2.draw()
    ghost3.draw()
    ghost4.draw()

    pygame.display.update()
    # time.sleep(0.01)

    if pacman.coordinate == ghost1.coordinate or pacman.coordinate == ghost2.coordinate or pacman.coordinate == ghost3.coordinate or pacman.coordinate == ghost4.coordinate:
        running = False
