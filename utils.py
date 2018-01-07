import display

BAT = 'B'
SNAKE = 'S'

def getPosInList(x, y):
    return (y * display.SCR_SIZE_X + x)

def getFirstStartingPos(map):
    playr = player()
    for x in range (display.SCR_SIZE_X):
        for y in range (display.SCR_SIZE_Y):
            if (map[getPosInList(x, y)] == '.'):
                player.pos_x = x
                player.pos_y = y
    player.gold = 0 # gold
    player.life = 100 # life
    player.maxLife = 100 # maxlife

    return player

def you_died(curses, win, stdscr, player):
    win.clear()
    win.addstr(display.SCR_SIZE_Y / 2, display.SCR_SIZE_X / 2 - 5, "YOU DIED !", curses.color_pair(4))
    win.refresh()
    c = 0
    while c != 27:
        c = stdscr.getch()
    win.clear()
    win.refresh()

class room:
    def __init__(s, i):
        s.number = i
        s.room_start_x = 0
        s.room_start_y = 0
        s.size_x = 0
        s.size_y = 0

class monster:
    def __init__(s, i):
        s.number = i
        s.pos_x = 0
        s.pos_y = 0
        s.type = 'A'
        s.attack = 0
        s.ennemy = False

class player:
    def __init__(s):
        s.pos_x = 0
        s.pos_y = 0
        s.life = 100
        s.maxLife = 100
        s.gold = 0
