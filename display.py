import main
import curses
import utils

SCR_SIZE_Y = 26
SCR_SIZE_X = 81

player = u'\u263A'.encode('utf-8')

def initCurses():
    stdscr = curses.initscr()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)

    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)
    stdscr.keypad(1)
    return stdscr

def addMapToWin(map, win):
    for x in range (0, SCR_SIZE_X):
        for y in range (0, SCR_SIZE_Y):
            pos = utils.getPosInList(x, y)
            if (map[pos] == '#'):
                win.addstr(y, x, "#", curses.color_pair(2))
            if (map[pos] == '.'):
                win.addstr(y, x, ".", curses.color_pair(3))
            if (map[pos] == '*'):
                win.addstr(y, x, "*", curses.color_pair(4))
    return win