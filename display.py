import main
import curses
import utils

SCR_SIZE_Y = 26
SCR_SIZE_X = 80

player = u'\u263A'.encode('utf-8')
door = u'\u256C'.encode('utf-8')
path = u'\u2591'.encode('utf-8')

def initCurses():
    stdscr = curses.initscr()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_BLUE, curses.COLOR_BLACK)

    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)
    stdscr.keypad(1)
    return stdscr

def addStatsToWin(win, player):
    win.addstr(SCR_SIZE_Y - 1, 0, "Life: %s(%s)               Gold: %s" \
        % (player[3], player[4], player[2]), curses.color_pair(1))
    return win

def addMapToWin(map, win):
    for x in range (0, SCR_SIZE_X):
        for y in range (0, SCR_SIZE_Y):
            pos = utils.getPosInList(x, y)
            if (map[pos] == u'\u2554'.encode('utf-8')):
                win.addstr(y, x, u'\u2554'.encode('utf-8'), curses.color_pair(2))
            if (map[pos] == u'\u255D'.encode('utf-8')):
                win.addstr(y, x, u'\u255D'.encode('utf-8'), curses.color_pair(2))
            if (map[pos] == u'\u2557'.encode('utf-8')):
                win.addstr(y, x, u'\u2557'.encode('utf-8'), curses.color_pair(2))
            if (map[pos] == u'\u255A'.encode('utf-8')):
                win.addstr(y, x, u'\u255A'.encode('utf-8'), curses.color_pair(2))
            if (map[pos] == u'\u2551'.encode('utf-8')):
                win.addstr(y, x, u'\u2551'.encode('utf-8'), curses.color_pair(2))
            if (map[pos] == u'\u2550'.encode('utf-8')):
                win.addstr(y, x, u'\u2550'.encode('utf-8'), curses.color_pair(2))
            if (map[pos] == '.'):
                win.addstr(y, x, ".", curses.color_pair(3))
            if (map[pos] == '*'):
                win.addstr(y, x, "*", curses.color_pair(1))
            if (map[pos] == u'\u2667'.encode('utf-8')):
                win.addstr(y, x, u'\u2667'.encode('utf-8'), curses.color_pair(4))
            if (map[pos] == 'B'):
                win.addstr(y, x, "B")
            if (map[pos] == 'S'):
                win.addstr(y, x, "S")
            if (map[pos] == u'\u25E2'.encode('utf-8')):
                win.addstr(y, x, u'\u25E2'.encode('utf-8'), curses.color_pair(5))
            if (map[pos] == door):
                win.addstr(y, x, door, curses.color_pair(2))
            if (map[pos] == path):
                win.addstr(y, x, path, curses.color_pair(2))
    return win
