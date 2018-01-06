import utils
import display
import random

def addRoom(map, room1_start_x, room1_start_y, size_x, size_y):
    x = room1_start_x
    y = room1_start_y
    for x in range(room1_start_x, room1_start_x + size_x):
        for y in range(room1_start_y, room1_start_y + size_y):
            pos = utils.getPosInList(x, y)
            if (x == room1_start_x or x == room1_start_x + size_x - 1):
                map[pos] = "#"
            elif (y == room1_start_y or y == room1_start_y + size_y - 1):
                map[pos] = "#"
            else:
                map[pos] = "."
    return map

def initMap():
    map = [' '] * (display.SCR_SIZE_X * display.SCR_SIZE_Y)
# 22 - 17
    y = 3
    while y < display.SCR_SIZE_Y - 20:
        x = 5
        while x < display.SCR_SIZE_X - 24:
            if random.randint(0, 1):
                map = addRoom(map, random.randint(x, x + 4), random.randint(y, y + 3), random.randint(10, 26), random.randint(6, 12))
            x += 31
        y += 18

    return map
