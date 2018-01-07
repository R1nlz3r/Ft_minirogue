import utils
import display
import random


def addRoom(map, room):
    if (room.size_x == 1):
        map[utils.getPosInList(room.room_start_x, room.room_start_y)] = '*'
    else:
        for x in range(room.room_start_x, room.room_start_x + room.size_x):
            for y in range(room.room_start_y, room.room_start_y + room.size_y):
                pos = utils.getPosInList(x, y)
                if (x == room.room_start_x or x == room.room_start_x + room.size_x - 1):
                    map[pos] = "#"
                elif (y == room.room_start_y or y == room.room_start_y + room.size_y - 1):
                    map[pos] = "#"
                else:
                    map[pos] = "."
    return map


def initMap():
    map = [' '] * (display.SCR_SIZE_X * display.SCR_SIZE_Y)

    rooms = placeRooms()
    for i in range(9):
        map = addRoom(map, rooms[i])
    map = placePaths(rooms, map)
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

    if (isTwoRoomsOfOneInSameColumn(size_x[0] * size_y[0], size_x[3] * size_y[3], size_x[6] * size_y[6])):
        return placeRooms()
    if (isTwoRoomsOfOneInSameColumn(size_x[1] * size_y[1], size_x[4] * size_y[4], size_x[7] * size_y[7])):
        return placeRooms()
    if (isTwoRoomsOfOneInSameColumn(size_x[2] * size_y[2], size_x[5] * size_y[5], size_x[8] * size_y[8])):
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
    if (roomTwo - roomOne == 1):
        if rooms[roomOne].size_x > 1:
            pos_x = rooms[roomOne].room_start_x + rooms[roomOne].size_x - 1
            pos_y = rooms[roomOne].room_start_y + random.randint(1, rooms[roomOne].size_y - 1)
        else:
            pos_x = rooms[roomOne].room_start_x
            pos_y = rooms[roomOne].room_start_y

        pos = utils.getPosInList(pos_x, pos_y)
        map[pos] = display.door

        if rooms[roomTwo].size_x > 1:
            pos_x = rooms[roomTwo].room_start_x
            pos_y = rooms[roomTwo].room_start_y + random.randint(1, rooms[roomTwo].size_y - 1)
        else:
            pos_x = rooms[roomTwo].room_start_x
            pos_y = rooms[roomTwo].room_start_y

        pos = utils.getPosInList(pos_x, pos_y)
        map[pos] = display.door
    else:
        if rooms[roomOne].size_x > 1:
            pos_x = rooms[roomOne].room_start_x + random.randint(1, rooms[roomOne].size_x - 1)
            pos_y = rooms[roomOne].room_start_y + rooms[roomOne].size_y - 1
        else:
            pos_x = rooms[roomOne].room_start_x
            pos_y = rooms[roomOne].room_start_y

        pos = utils.getPosInList(pos_x, pos_y)
        map[pos] = display.door

        if rooms[roomTwo].size_x > 1:
            pos_x = rooms[roomTwo].room_start_x + random.randint(1, rooms[roomTwo].size_x - 1)
            pos_y = rooms[roomTwo].room_start_y
        else:
            pos_x = rooms[roomTwo].room_start_x
            pos_y = rooms[roomTwo].room_start_y

        pos = utils.getPosInList(pos_x, pos_y)
        map[pos] = display.door
    return map

