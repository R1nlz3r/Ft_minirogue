import utils
import display
import random

def initMap():
    map = [' '] * (display.SCR_SIZE_X * display.SCR_SIZE_Y)
    rooms = placeRooms()
    for i in range(9):
        map = addRoom(map, rooms[i])
    map = placePaths(rooms, map)
    map = placeObjects(map)
    map = placeAi(map)
    return map

def placeAi(map):
    for x in range (0, display.SCR_SIZE_X):
        for y in range (0, display.SCR_SIZE_Y - 1):
            pos = utils.getPosInList(x, y)
            if (map[pos] == '.' and random.randint(0, 200) == 1):
                map[pos] = 'B'
            if (map[pos] == '.' and random.randint(0, 200) == 1):
                map[pos] = 'S'
    return map

def placeObjects(map):
    for x in range (0, display.SCR_SIZE_X):
        for y in range (0, display.SCR_SIZE_Y - 1):
            pos = utils.getPosInList(x, y)
            if (map[pos] == '.' and random.randint(0, 140) == 1):
                map[pos] = "*"
            if (map[pos] == '.' and random.randint(0, 150) == 1):
                map[pos] = u'\u2667'.encode('utf-8')
    return map

def addRoom(map, room):
    if (room.size_x != 1):
        for x in range(room.room_start_x, room.room_start_x + room.size_x):
            for y in range(room.room_start_y, room.room_start_y + room.size_y):
                pos = utils.getPosInList(x, y)
                if (x == room.room_start_x or x == room.room_start_x + room.size_x - 1):
                    map[pos] = "#"
                elif (y == room.room_start_y or y == room.room_start_y + room.size_y - 1):
                    map[pos] = "#"
                if (x == room.room_start_x and y == room.room_start_y):
                    map[pos] = u'\u2554'.encode('utf-8')
                elif (x == room.room_start_x + room.size_x - 1 and y == room.room_start_y + room.size_y - 1):
                    map[pos] = u'\u255D'.encode('utf-8')
                elif (x == room.room_start_x + room.size_x - 1 and y == room.room_start_y):
                    map[pos] = u'\u2557'.encode('utf-8')
                elif (x == room.room_start_x and y == room.room_start_y + room.size_y - 1):
                    map[pos] = u'\u255A'.encode('utf-8')
                elif (x == room.room_start_x or x == room.room_start_x + room.size_x - 1):
                    map[pos] = u'\u2551'.encode('utf-8')
                elif (y == room.room_start_y or y == room.room_start_y + room.size_y - 1):
                    map[pos] = u'\u2550'.encode('utf-8')
                else:
                    map[pos] = "."
    return map

def isTwoRoomsOfOneInSameColumn(a, b, c):
    if ((a + b == 2) or (a + c == 2) or (b + c == 2)):
        return True
    return False


def placeRooms():
    size_x = [0] * 9
    size_y = [0] * 9
    rooms = [utils.room(0)] * 9

    for i in range(9):
        size_x[i] = random.randint(3, 26)
        size_y[i] = random.randint(3, 7)
        if (size_x[i] <= 3 or size_y[i] <= 3):
            size_y[i] = 1
            size_x[i] = 1
        rooms[i] = utils.room(i)

    if (isTwoRoomsOfOneInSameColumn(size_x[0] * size_y[0], \
        size_x[3] * size_y[3], size_x[6] * size_y[6])):
        return placeRooms()
    if (isTwoRoomsOfOneInSameColumn(size_x[1] * size_y[1], \
        size_x[4] * size_y[4], size_x[7] * size_y[7])):
        return placeRooms()
    if (isTwoRoomsOfOneInSameColumn(size_x[2] * size_y[2], \
        size_x[5] * size_y[5], size_x[8] * size_y[8])):
        return placeRooms()

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
            rooms[i + j * 3].room_start_x = random_size_x
            rooms[i + j * 3].room_start_y = random_size_y
            rooms[i + j * 3].size_x = room_size_x
            rooms[i + j * 3].size_y = room_size_y

    return rooms


def checkPaths(roomsConnected, paths, tried, currentRoom):
    if (tried > 9):
        return roomsConnected

    if (currentRoom == 4):
        if (paths[6] == True and roomsConnected[5] == False):
            roomsConnected[5] = True
            roomsConnected = checkPaths(roomsConnected, paths, tried + 1, 5)
        if (paths[3] == True and roomsConnected[1] == False):
            roomsConnected[1] = True
            roomsConnected = checkPaths(roomsConnected, paths, tried + 1, 1)
        if (paths[5] == True and roomsConnected[3] == False):
            roomsConnected[3] = True
            roomsConnected = checkPaths(roomsConnected, paths, tried + 1, 3)
        if (paths[8] == True and roomsConnected[7] == False):
            roomsConnected[7] = True
            roomsConnected = checkPaths(roomsConnected, paths, tried + 1, 7)
    if (currentRoom == 1):
        if (paths[0] == True and roomsConnected[0] == False):
            roomsConnected[0] = True
            roomsConnected = checkPaths(roomsConnected, paths, tried + 1, 0)
        if (paths[1] == True and roomsConnected[2] == False):
            roomsConnected[2] = True
            roomsConnected = checkPaths(roomsConnected, paths, tried + 1, 2)
    if (currentRoom == 3):
        if (paths[2] == True and roomsConnected[0] == False):
            roomsConnected[0] = True
            roomsConnected = checkPaths(roomsConnected, paths, tried + 1, 0)
        if (paths[7] == True and roomsConnected[6] == False):
            roomsConnected[6] = True
            roomsConnected = checkPaths(roomsConnected, paths, tried + 1, 6)
    if (currentRoom == 7):
        if (paths[10] == True and roomsConnected[6] == False):
            roomsConnected[6] = True
            roomsConnected = checkPaths(roomsConnected, paths, tried + 1, 6)
        if (paths[11] == True and roomsConnected[8] == False):
            roomsConnected[8] = True
            roomsConnected = checkPaths(roomsConnected, paths, tried + 1, 8)
    if (currentRoom == 5):
        if (paths[4] == True and roomsConnected[2] == False):
            roomsConnected[2] = True
            roomsConnected = checkPaths(roomsConnected, paths, tried + 1, 2)
        if (paths[9] == True and roomsConnected[8] == False):
            roomsConnected[8] = True
            roomsConnected = checkPaths(roomsConnected, paths, tried + 1, 8)
    if (currentRoom == 0):
        if (paths[0] == True and roomsConnected[1] == False):
            roomsConnected[1] = True
            roomsConnected = checkPaths(roomsConnected, paths, tried + 1, 1)
        if (paths[2] == True and roomsConnected[3] == False):
            roomsConnected[3] = True
            roomsConnected = checkPaths(roomsConnected, paths, tried + 1, 3)
    if (currentRoom == 2):
        if (paths[1] == True and roomsConnected[1] == False):
            roomsConnected[1] = True
            roomsConnected = checkPaths(roomsConnected, paths, tried + 1, 1)
        if (paths[4] == True and roomsConnected[5] == False):
            roomsConnected[5] = True
            roomsConnected = checkPaths(roomsConnected, paths, tried + 1, 5)
    if (currentRoom == 8):
        if (paths[9] == True and roomsConnected[5] == False):
            roomsConnected[5] = True
            roomsConnected = checkPaths(roomsConnected, paths, tried + 1, 5)
        if (paths[11] == True and roomsConnected[7] == False):
            roomsConnected[7] = True
            roomsConnected = checkPaths(roomsConnected, paths, tried + 1, 7)
    if (currentRoom == 6):
        if (paths[7] == True and roomsConnected[3] == False):
            roomsConnected[3] = True
            roomsConnected = checkPaths(roomsConnected, paths, tried + 1, 3)
        if (paths[10] == True and roomsConnected[7] == False):
            roomsConnected[7] = True
            roomsConnected = checkPaths(roomsConnected, paths, tried + 1, 7)

    return roomsConnected

def placePaths(rooms, map):
    numberOfPaths = 0
    paths = [False] * 12
    randomNumberOfPaths = random.randint(8, 11)

    while numberOfPaths < randomNumberOfPaths:
        newPathNumber = random.randint(0, 11)
        if (paths[newPathNumber] == False):
            paths[newPathNumber] = True
            numberOfPaths += 1
    roomsConnected = [False] * 9
    beginningRoom = 4
    roomsConnected[beginningRoom] = True
    tried = 0
    roomsConnected = checkPaths(roomsConnected, paths, tried, beginningRoom)

    numberOfConnectedRooms = 0
    for i in range(9):
        if (roomsConnected[i] == True):
            numberOfConnectedRooms += 1

    if (numberOfConnectedRooms != 9):
        placePaths(rooms, map)
    else :
        for i in range (12):
            if (paths[i] == True):
                map = placeDoors(i, rooms, map)

    return map

def placeDoors(pathNumber, rooms, map):
    roomOne = 0
    roomTwo = 0

    if (pathNumber == 0):
        roomOne = 0
        roomTwo = 1
    elif (pathNumber == 1):
        roomOne = 1
        roomTwo = 2
    elif (pathNumber == 2):
        roomOne = 0
        roomTwo = 3
    elif (pathNumber == 3):
        roomOne = 1
        roomTwo = 4
    elif (pathNumber == 4):
        roomOne = 2
        roomTwo = 5
    elif (pathNumber == 5):
        roomOne = 3
        roomTwo = 4
    elif (pathNumber == 6):
        roomOne = 4
        roomTwo = 5
    elif (pathNumber == 7):
        roomOne = 3
        roomTwo = 6
    elif (pathNumber == 8):
        roomOne = 4
        roomTwo = 7
    elif (pathNumber == 9):
        roomOne = 5
        roomTwo = 8
    elif (pathNumber == 10):
        roomOne = 6
        roomTwo = 7
    elif (pathNumber == 11):
        roomOne = 7
        roomTwo = 8
    return placeDoorsOnMap(roomOne, roomTwo, rooms, map)

def placeDoorsOnMap(roomOne, roomTwo, rooms, map):
    pos_x_one = 0
    pos_y_one = 0
    pos_x_two = 0
    pos_y_two = 0
    if (roomTwo - roomOne == 1):
        if rooms[roomOne].size_x > 1:
            pos_x_one = rooms[roomOne].room_start_x + rooms[roomOne].size_x - 1
            pos_y_one = rooms[roomOne].room_start_y + random.randint(2, rooms[roomOne].size_y - 2)
            pos = utils.getPosInList(pos_x_one, pos_y_one)
            map[pos] = display.door
        else:
            pos_x_one = rooms[roomOne].room_start_x
            pos_y_one = rooms[roomOne].room_start_y
            pos = utils.getPosInList(pos_x_one, pos_y_one)
            map[pos] = display.path

        if rooms[roomTwo].size_x > 1:
            pos_x_two = rooms[roomTwo].room_start_x
            pos_y_two = rooms[roomTwo].room_start_y + random.randint(2, rooms[roomTwo].size_y - 2)
            pos = utils.getPosInList(pos_x_two, pos_y_two)
            map[pos] = display.door
        else:
            pos_x_two = rooms[roomTwo].room_start_x
            pos_y_two = rooms[roomTwo].room_start_y
            pos = utils.getPosInList(pos_x_two, pos_y_two)
            map[pos] = display.path
        draw_path_east(map, pos_x_one, pos_y_one, pos_x_two, pos_y_two)
    else:
        if rooms[roomOne].size_x > 1:
            pos_x_one = rooms[roomOne].room_start_x + random.randint(2, rooms[roomOne].size_x - 2)
            pos_y_one = rooms[roomOne].room_start_y + rooms[roomOne].size_y - 1
            pos = utils.getPosInList(pos_x_one, pos_y_one)
            map[pos] = display.door
        else:
            pos_x_one = rooms[roomOne].room_start_x
            pos_y_one = rooms[roomOne].room_start_y
            pos = utils.getPosInList(pos_x_one, pos_y_one)
            map[pos] = display.path

        if rooms[roomTwo].size_x > 1:
            pos_x_two = rooms[roomTwo].room_start_x + random.randint(2, rooms[roomTwo].size_x - 2)
            pos_y_two = rooms[roomTwo].room_start_y
            pos = utils.getPosInList(pos_x_two, pos_y_two)
            map[pos] = display.door
        else:
            pos_x_two = rooms[roomTwo].room_start_x
            pos_y_two = rooms[roomTwo].room_start_y
            pos = utils.getPosInList(pos_x_two, pos_y_two)
            map[pos] = display.path
        draw_path_south(map, pos_x_one, pos_y_one, pos_x_two, pos_y_two)

    return map

def draw_path_east(map, pos_x_one, pos_y_one, pos_x_two, pos_y_two):
    move_before_turn = random.randint(1, pos_x_two - pos_x_one - 1)
    current_pos_x = pos_x_one
    current_pos_y = pos_y_one

    for i in range(move_before_turn):
        current_pos_x += 1
        map[utils.getPosInList(current_pos_x, current_pos_y)] = display.path
    while current_pos_y < pos_y_two:
        current_pos_y += 1
        map[utils.getPosInList(current_pos_x, current_pos_y)] = display.path
    while current_pos_y > pos_y_two:
        current_pos_y -= 1
        map[utils.getPosInList(current_pos_x, current_pos_y)] = display.path
    while current_pos_x < pos_x_two:
        map[utils.getPosInList(current_pos_x, current_pos_y)] = display.path
        current_pos_x += 1

def draw_path_south(map, pos_x_one, pos_y_one, pos_x_two, pos_y_two):
    move_before_turn = random.randint(1, pos_y_two - pos_y_one - 1)
    current_pos_x = pos_x_one
    current_pos_y = pos_y_one

    for i in range(move_before_turn):
        current_pos_y += 1
        map[utils.getPosInList(current_pos_x, current_pos_y)] = display.path

    while current_pos_x < pos_x_two:
        current_pos_x += 1
        map[utils.getPosInList(current_pos_x, current_pos_y)] = display.path
    while current_pos_x > pos_x_two:
        current_pos_x -= 1
        map[utils.getPosInList(current_pos_x, current_pos_y)] = display.path
    while current_pos_y < pos_y_two:
        map[utils.getPosInList(current_pos_x, current_pos_y)] = display.path
        current_pos_y += 1



