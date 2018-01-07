import display

def getPosInList(x, y):
    return (y * display.SCR_SIZE_X + x)

def getFirstStartingPos(map):
    player = [0] * 5
    for x in range (display.SCR_SIZE_X):
        for y in range (display.SCR_SIZE_Y):
            if (map[getPosInList(x, y)] == '.'):
                player[0] = x
                player[1] = y
    player[2] = 0 # gold
    player[3] = 100 # life
    player[4] = 100 # maxlife

    return player

class room:
    def __init__(s, i):
        s.number = i
        s.room_start_x = 0
        s.room_start_y = 0
        s.size_x = 0
        s.size_y = 0