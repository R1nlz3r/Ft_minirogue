import display
import random

BAT = 'B'
SNAKE = 'S'

def is_monster(pos, monsters):
    for i in range(20):
        pos_monster = getPosInList(monsters[i].pos_x, monsters[i].pos_y)
        if (pos_monster == pos and monsters[i].life > 0):
            return True
    return False

def which_monster(pos, monsters):
    for i in range(20):
        pos_monster = getPosInList(monsters[i].pos_x, monsters[i].pos_y)
        if (pos_monster == pos):
            return i
    return 19

def getPosInList(x, y):
    return (y * display.SCR_SIZE_X + x)

def getRandomDot(map):
    pos_monster = [0] * 2
    nbDot = 0

    for y in range (display.SCR_SIZE_Y - 1):
        for x in range (display.SCR_SIZE_X):
            pos = getPosInList(x, y)
            if (map[pos] == '.'):
                nbDot += 1

    chosen_dot = random.randint(1, nbDot)

    nbDot = 0

    for y in range(display.SCR_SIZE_Y - 1):
        for x in range(display.SCR_SIZE_X):
            pos = getPosInList(x, y)
            if (map[pos] == '.'):
                nbDot += 1
            if (nbDot == chosen_dot):
                pos_monster[0] = x
                pos_monster[1] = y
                return pos_monster

    return pos_monster

def getFirstStartingPos(map, playr):
    for x in range (display.SCR_SIZE_X):
        for y in range (display.SCR_SIZE_Y):
            if (map[getPosInList(x, y)] == '.'):
                playr.pos_x = x
                playr.pos_y = y

    return playr

def you_died(curses, win, stdscr, player):
    win.clear()
    win.addstr(display.SCR_SIZE_Y / 2, display.SCR_SIZE_X / 2 - 5, "YOU DIED !", curses.color_pair(4))
    win.addstr(display.SCR_SIZE_Y / 2 + 1, display.SCR_SIZE_X / 10, "you had %d gold coins, killed %d monsters and went down to level %d" % (player.gold, player.kill, player.level), curses.color_pair(1))
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
        s.life = 0

class player:
    def __init__(s):
        s.pos_x = 0
        s.pos_y = 0
        s.life = 100
        s.maxLife = 100
        s.gold = 0
        s.attack = 3
        s.turns = 0
        s.level = 1
        s.kill = 0
