'''
The classes module.

Contains Wall and Path tile blocks.

Contains the pacman class.

A ghost class.

Classes for each of the ghosts in pacman,
Blinky, Inky, Pinky, Clyde.
Each ghost class inherits the generic Ghost class.
'''

from utils import *

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
# ------------------------------------------------------- Pacman Class --------------------------------------------------


class Pacman():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.coordinate = (x, y)
        self.direction = (1, 0)
        self.next = get_block(self.coordinate, self.direction)
        self.sprite = pacman_l
        self.mouth_open = False
        self.tmpdirection = (1,0)


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
        else:
            i,j = get_block(self.coordinate, self.tmpdirection)
            if maze[j][i] == 0:
                self.direction = self.tmpdirection
                self.coordinate = get_block(self.coordinate, self.direction)

        self.next = get_block(self.coordinate, self.direction)
        # screen.blit(self.sprite, coor_to_px(self.coordinate))

    def draw(self):
        screen.blit(self.sprite, coor_to_px(self.coordinate))


# ------------------------------------------------------- Ghost Classes --------------------------------------------------
# Ghost Class
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
        self.mode = 'chase'
        self.home = (2, 3)
        self.counter = 1
        self.threshold = get_threshold(self.counter)

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
        # Sprite Update
        if self.mode == 'chase':
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
                

        if self.mode == 'scatter':
            if self.phase_1:
                if self.direction == (1, 0):
                    self.sprite = scared_1_b
                if self.direction == (-1, 0):
                    self.sprite = scared_1_b
                if self.direction == (0, 1):
                    self.sprite = scared_1_b
                if self.direction == (0, -1):
                    self.sprite = scared_1_b
            else:
                if self.direction == (1, 0):
                    self.sprite = scared_1_b
                if self.direction == (-1, 0):
                    self.sprite = scared_1_b
                if self.direction == (0, 1):
                    self.sprite = scared_1_b
                if self.direction == (0, -1):
                    self.sprite = scared_1_b
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

        self.counter += 1

        if self.counter == self.threshold:
            if get_threshold(self.counter) == 0:
                self.mode = 'chase'
                self.choose_target_tile()
                self.threshold += get_threshold(self.counter)
            else:
                #print("This code was accessed")
                self.threshold += get_threshold(self.counter)
                if self.mode == 'chase':
                    self.mode = 'scatter'
                    self.choose_target_tile()
                    self.direction = change_direction(self.direction)
                elif self.mode == 'scatter':
                    self.mode = 'chase'
                    self.choose_target_tile()
                    self.direction = change_direction(self.direction)
                elif get_threshold(self.counter) == 0:
                    self.mode = 'chase'
                    self.choose_target_tile()
                    self.direction = change_direction(self.direction)

    def choose_target_tile(self):
        if self.mode == 'chase':
            self.find_target()
        if self.mode == 'scatter':
            self.target = self.home

    def set_home(self, coor_tuple):
        self.home = coor_tuple

    def find_target(self):
        self.target = pacman.coordinate


# ------------------------------------------------------- Blinky Class --------------------------------------------------
class Blinky(Ghost):
    pass


# ------------------------------------------------------- Inky Class --------------------------------------------------
class inky(Ghost):
    def update(self):
        self.find_target()
        # Sprite Update
        if self.mode == 'chase':
            if self.phase_1:
                if self.direction == (1, 0):
                    self.sprite = inky_1_r
                if self.direction == (-1, 0):
                    self.sprite = inky_1_l
                if self.direction == (0, 1):
                    self.sprite = inky_1_d
                if self.direction == (0, -1):
                    self.sprite = inky_1_u
            else:
                if self.direction == (1, 0):
                    self.sprite = inky_2_r
                if self.direction == (-1, 0):
                    self.sprite = inky_2_l
                if self.direction == (0, 1):
                    self.sprite = inky_2_d
                if self.direction == (0, -1):
                    self.sprite = inky_2_u
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

        if self.mode == 'scatter':
            if self.phase_1:
                if self.direction == (1, 0):
                    self.sprite = scared_1_b
                if self.direction == (-1, 0):
                    self.sprite = scared_1_b
                if self.direction == (0, 1):
                    self.sprite = scared_1_b
                if self.direction == (0, -1):
                    self.sprite = scared_1_b
            else:
                if self.direction == (1, 0):
                    self.sprite = scared_1_b
                if self.direction == (-1, 0):
                    self.sprite = scared_1_b
                if self.direction == (0, 1):
                    self.sprite = scared_1_b
                if self.direction == (0, -1):
                    self.sprite = scared_1_b
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

        self.counter += 1

        if self.counter == self.threshold:
            if get_threshold(self.counter) == 0:
                self.mode = 'chase'
                self.choose_target_tile()
                self.threshold += get_threshold(self.counter)
            else:
                self.threshold += get_threshold(self.counter)
                if self.mode == 'chase':
                    self.mode = 'scatter'
                    self.choose_target_tile()
                    self.direction = change_direction(self.direction)
                elif self.mode == 'scatter':
                    self.mode = 'chase'
                    self.choose_target_tile()
                    self.direction = change_direction(self.direction)
                elif get_threshold(self.counter) == 0:
                    self.mode = 'chase'
                    self.choose_target_tile()
                    self.direction = change_direction(self.direction)

    def find_target(self):
        vector = get_vector(pacman.coordinate, blinky.coordinate)
        self.target = get_block(pacman.coordinate, vector)


# ------------------------------------------------------- Pinky Class --------------------------------------------------
class Pinky(Ghost):
    def update(self):
        # Sprite Update
        if self.mode == 'chase':
            self.find_target()
            if self.phase_1:
                if self.direction == (1, 0):
                    self.sprite = pinky_1_r
                if self.direction == (-1, 0):
                    self.sprite = pinky_1_l
                if self.direction == (0, 1):
                    self.sprite = pinky_1_d
                if self.direction == (0, -1):
                    self.sprite = pinky_1_u
            else:
                if self.direction == (1, 0):
                    self.sprite = pinky_2_r
                if self.direction == (-1, 0):
                    self.sprite = pinky_2_l
                if self.direction == (0, 1):
                    self.sprite = pinky_2_d
                if self.direction == (0, -1):
                    self.sprite = pinky_2_u
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

        if self.mode == 'scatter':
            if self.phase_1:
                if self.direction == (1, 0):
                    self.sprite = scared_1_b
                if self.direction == (-1, 0):
                    self.sprite = scared_1_b
                if self.direction == (0, 1):
                    self.sprite = scared_1_b
                if self.direction == (0, -1):
                    self.sprite = scared_1_b
            else:
                if self.direction == (1, 0):
                    self.sprite = scared_1_b
                if self.direction == (-1, 0):
                    self.sprite = scared_1_b
                if self.direction == (0, 1):
                    self.sprite = scared_1_b
                if self.direction == (0, -1):
                    self.sprite = scared_1_b
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

        self.counter += 1

        if self.counter == self.threshold:
            if get_threshold(self.counter) == 0:
                self.mode = 'chase'
                self.choose_target_tile()
                self.threshold += get_threshold(self.counter)
            else:
                self.threshold += get_threshold(self.counter)
                if self.mode == 'chase':
                    self.mode = 'scatter'
                    self.choose_target_tile()
                    self.direction = change_direction(self.direction)
                elif self.mode == 'scatter':
                    self.mode = 'chase'
                    self.choose_target_tile()
                    self.direction = change_direction(self.direction)
                elif get_threshold(self.counter) == 0:
                    self.mode = 'chase'
                    self.choose_target_tile()
                    self.direction = change_direction(self.direction)

    def find_target(self):
        # i, j = get_block(pacman.coordinate, pacman.direction)
        # self.target = pacman.coordinate
        # a = 0
        # while maze[j][i] == 0 and a < 4:
        #     self.target = get_block(self.target, pacman.direction)
        #     i, j = get_block(self.target, self.direction)
        #     a += 1
        self.target = get_block(pacman.coordinate,pacman.direction)
        self.target = get_block(self.target,pacman.direction)
        self.target = get_block(self.target,pacman.direction)
        self.target = get_block(self.target,pacman.direction)


# ------------------------------------------------------- Clyde Class --------------------------------------------------
class Clyde(Ghost):
    def update(self):
        # Sprite Update
        if self.mode == 'chase':
            self.find_target()
            if self.phase_1:
                if self.direction == (1, 0):
                    self.sprite = clyde_1_r
                if self.direction == (-1, 0):
                    self.sprite = clyde_1_l
                if self.direction == (0, 1):
                    self.sprite = clyde_1_d
                if self.direction == (0, -1):
                    self.sprite = clyde_1_u
            else:
                if self.direction == (1, 0):
                    self.sprite = clyde_2_r
                if self.direction == (-1, 0):
                    self.sprite = clyde_2_l
                if self.direction == (0, 1):
                    self.sprite = clyde_2_d
                if self.direction == (0, -1):
                    self.sprite = clyde_2_u
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

        if self.mode == 'scatter':
            if self.phase_1:
                if self.direction == (1, 0):
                    self.sprite = scared_1_b
                if self.direction == (-1, 0):
                    self.sprite = scared_1_b
                if self.direction == (0, 1):
                    self.sprite = scared_1_b
                if self.direction == (0, -1):
                    self.sprite = scared_1_b
            else:
                if self.direction == (1, 0):
                    self.sprite = scared_1_b
                if self.direction == (-1, 0):
                    self.sprite = scared_1_b
                if self.direction == (0, 1):
                    self.sprite = scared_1_b
                if self.direction == (0, -1):
                    self.sprite = scared_1_b
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

        self.counter += 1

        if self.counter == self.threshold:
            if get_threshold(self.counter) == 0:
                self.mode = 'chase'
                self.choose_target_tile()
                self.threshold += get_threshold(self.counter)
            else:
                self.threshold += get_threshold(self.counter)
                if self.mode == 'chase':
                    self.mode = 'scatter'
                    self.choose_target_tile()
                    self.direction = change_direction(self.direction)
                elif self.mode == 'scatter':
                    self.mode = 'chase'
                    self.choose_target_tile()
                    self.direction = change_direction(self.direction)
                elif get_threshold(self.counter) == 0:
                    self.mode = 'chase'
                    self.choose_target_tile()
                    self.direction = change_direction(self.direction)

    def find_target(self):
        if distance(self.coordinate, pacman.coordinate) >= 8:
            self.target = pacman.coordinate
        else:
            self.target = self.home


# Initialise characters
pacman = Pacman(13, 19)
pac_upd = 0
blinky = Blinky(13, 11)
inky = inky(13, 7)
inky.set_home((24, 3))
pinky = Pinky(3, 22)
pinky.set_home((2, 26))
clyde = Clyde(23, 22)
clyde.set_home((24, 26))

entities = [pacman, blinky, inky, pinky, clyde]
# entities = [pacman, inky, blinky]
