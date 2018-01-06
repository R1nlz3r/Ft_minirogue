import utils
import display

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

    map = addRoom(map, 8, 10, 15, 8)

    return map