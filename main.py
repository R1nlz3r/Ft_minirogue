import curses
import mapGenerator
import display
import locale
import utils

locale.setlocale(locale.LC_ALL, '')

def run(win, map, stdscr):
    player = utils.getFirstStartingPos(map) 

    win.addstr(player[1], player[0], display.player, curses.color_pair(1))
    win.refresh()

    while True:
        c = stdscr.getch()
        pos = utils.getPosInList(player[0], player[1])
        if c == 27:
            break
        if c == curses.KEY_DOWN and player[1] < display.SCR_SIZE_Y - 2:
            #if (map[pos + display.SCR_SIZE_X] != '#'):
            player[1] += 1
        if c == curses.KEY_UP and player[1] > 0:
            #if (map[pos - display.SCR_SIZE_X] != '#'):
            player[1] -= 1
        if c == curses.KEY_RIGHT and player[0] < display.SCR_SIZE_X - 2:
            #if (map[pos + 1] != '#'):
            player[0] += 1
        if c == curses.KEY_LEFT and player[0] > 0:
            #if (map[pos - 1] != '#'):
            player[0] -= 1
        win.clear()
        win = display.addMapToWin(map, win)
        win.addstr(player[1], player[0], display.player, curses.color_pair(1))
        win.refresh()

def main():
    stdscr = display.initCurses()

    map = mapGenerator.initMap()

    win = curses.newwin(display.SCR_SIZE_Y, display.SCR_SIZE_X)

    run(win, map, stdscr)

    curses.nocbreak()
    stdscr.keypad(0)
    curses.echo()

if __name__ == "__main__":
    main()
