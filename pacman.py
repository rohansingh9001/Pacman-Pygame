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

__version__ = '0.23'


import pygame
import time
from utils import *
from entities import *


# Game Loop
running = True

while running:

    for entity in entities[1:]:
        if pacman.coordinate == entity.coordinate:
            running = False

    for ghost in entities[1:]:
        if ghost.target == ghost.coordinate:
            ghost.choose_target_tile()

    for entity in entities:
        if entity.coordinate == (23, 13):
            entity.coordinate = (4, 13)
        elif entity.coordinate == (3, 13):
            entity.coordinate = (22, 13)

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

    if pac_upd == 30:
        for entity in entities:
            entity.update()
            for entity in entities[1:]:
                if pacman.coordinate == entity.coordinate:
                    running = False
        pac_upd = 0

    pac_upd += 1

    for entity in entities:
        entity.draw()
    # print("Pinky", pinky.target, pacman.coordinate)
    # print("Blinky",blinky.target,pacman.coordinate)
    # print("inky",inky.target,pacman.coordinate)
    # print("Clyde",clyde.target,pacman.coordinate)
    pygame.display.update()
    # time.sleep(0.01)
