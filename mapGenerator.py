import utils
import display
import random


def addRoom(map, room_start_x, room_start_y, size_x, size_y):
    if (size_x == 1):
        map[utils.getPosInList(room_start_x, room_start_y)] = '*'
    else:
        for x in range(room_start_x, room_start_x + size_x):
            print("\n")
            for y in range(room_start_y, room_start_y + size_y):
                pos = utils.getPosInList(x, y)
                if (x == room_start_x or x == room_start_x + size_x - 1):
                    map[pos] = "#"
                elif (y == room_start_y or y == room_start_y + size_y - 1):
                    map[pos] = "#"
                else:
                    map[pos] = "."
    return map


def initMap():
    map = [' '] * (display.SCR_SIZE_X * display.SCR_SIZE_Y)

    # map = addRoom(map, 50, 15, 15, 8)

    # map = addRoom(map, 5, 6, 40, 4)

    map = placeRooms(map)

    return map


def isTwoRoomsOfOneInSameColumn(a, b, c):
    if ((a + b == 2) or (a + c == 2) or (b + c == 2)):
        return True
    return False


def placeRooms(map):
    print(display.SCR_SIZE_X * display.SCR_SIZE_Y)
    size_x = [0] * 9
    size_y = [0] * 9

    for i in range(9):
        size_x[i] = random.randint(3, 26)
        size_y[i] = random.randint(3, 7)
        if (size_x[i] <= 3 or size_y[i] <= 3):
            size_y[i] = 1
            size_x[i] = 1

    if (isTwoRoomsOfOneInSameColumn(size_x[0] * size_y[0], size_x[3] * size_y[3], size_x[6] * size_y[6])):
        return placeRooms(map)
    if (isTwoRoomsOfOneInSameColumn(size_x[1] * size_y[1], size_x[4] * size_y[4], size_x[7] * size_y[7])):
        return placeRooms(map)
    if (isTwoRoomsOfOneInSameColumn(size_x[2] * size_y[2], size_x[5] * size_y[5], size_x[8] * size_y[8])):
        return placeRooms(map)

    for i in range(3):
        for j in range(3):
            room_size_x = size_x[i + 3 * j]
            room_size_y = size_y[i + 3 * j]
            room_start_x_min = i * 27
            room_start_x_max = 25 + (i * 27) - room_size_x
            room_start_y_min = 8 * j
            room_start_y_max = 6 + (j * 8) - room_size_y
            if (room_start_x_max <= room_start_x_min):
                random_size_x = i * 27
            else:
                random_size_x = random.randint(room_start_x_min, room_start_x_max)
            if (room_start_y_max <= room_start_y_min):
                random_size_y = j * 8
            else:
                random_size_y = random.randint(room_start_y_min, room_start_y_max)
                # if (random_size_y > 26):
                #   print(room_start_y_min)
                #   print(room_start_y_max)
            map = addRoom(map, random_size_x, random_size_y, room_size_x, room_size_y)

    return map
