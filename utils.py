import display

LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3

def getPosInList(x, y):
    return (y * display.SCR_SIZE_X + x)

def getFirstStartingPos(map):
    player = [0, 0]
    for x in range (display.SCR_SIZE_X):
        for y in range (display.SCR_SIZE_Y):
            if (map[getPosInList(x, y)] == '.'):
                player[0] = x
                player[1] = y
    return player

class room:
    def __init__(s, i):
        s.number = i
        s.room_start_x = 0
        s.room_start_y = 0
        s.size_x = 0
        s.size_y = 0
        s.door_n = False
        s.door_e = False
        s.door_s = False
        s.door_w = False