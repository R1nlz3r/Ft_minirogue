import curses
import mapGenerator
import display
import locale
import utils

import time

locale.setlocale(locale.LC_ALL, '')

def run(win, map, stdscr):
    map = mapGenerator.initMap()
    player = utils.getFirstStartingPos(map)

    win.clear()
    win = display.addMapToWin(map, win)
    win = display.addStatsToWin(win, player)
    win.addstr(player[1], player[0], display.player, curses.color_pair(1))
    win.refresh()

    time.sleep(1)
    c = stdscr.getch()
    while True:
        pos = utils.getPosInList(player[0], player[1])
        if c == 27:
            win.clear()
            win.refresh()
            break
        if c == curses.KEY_DOWN and player[1] < display.SCR_SIZE_Y - 2:
            if not (map[pos + display.SCR_SIZE_X] == u'\u2550'.encode('utf-8') \
                or map[pos + display.SCR_SIZE_X] == u'\u2551'.encode('utf-8') \
                or map[pos + display.SCR_SIZE_X] == u'\u2554'.encode('utf-8') \
                or map[pos + display.SCR_SIZE_X] == u'\u255D'.encode('utf-8') \
                or map[pos + display.SCR_SIZE_X] == u'\u2557'.encode('utf-8') \
                or map[pos + display.SCR_SIZE_X] == u'\u255A'.encode('utf-8') \
                or map[pos + display.SCR_SIZE_X] == 'S' \
                or map[pos + display.SCR_SIZE_X] == 'B' \
                or map[pos + display.SCR_SIZE_X] == ' '):
                player[1] += 1
        if c == curses.KEY_UP and player[1] > 0:
            if not (map[pos - display.SCR_SIZE_X] == u'\u2550'.encode('utf-8') \
                or map[pos - display.SCR_SIZE_X] == u'\u2551'.encode('utf-8') \
                or map[pos - display.SCR_SIZE_X] == u'\u2554'.encode('utf-8') \
                or map[pos - display.SCR_SIZE_X] == u'\u255D'.encode('utf-8') \
                or map[pos - display.SCR_SIZE_X] == u'\u2557'.encode('utf-8') \
                or map[pos - display.SCR_SIZE_X] == u'\u255A'.encode('utf-8') \
                or map[pos - display.SCR_SIZE_X] == 'S' \
                or map[pos - display.SCR_SIZE_X] == 'B' \
                or map[pos - display.SCR_SIZE_X] == ' '):
                player[1] -= 1
        if c == curses.KEY_RIGHT and player[0] < display.SCR_SIZE_X - 2:
            if not (map[pos + 1] == u'\u2550'.encode('utf-8') \
                or map[pos + 1] == u'\u2551'.encode('utf-8') \
                or map[pos + 1] == u'\u2554'.encode('utf-8') \
                or map[pos + 1] == u'\u255D'.encode('utf-8') \
                or map[pos + 1] == u'\u2557'.encode('utf-8') \
                or map[pos + 1] == u'\u255A'.encode('utf-8') \
                or map[pos + 1] == 'S' \
                or map[pos + 1] == 'B' \
                or map[pos + 1] == ' '):
                player[0] += 1
        if c == curses.KEY_LEFT and player[0] > 0:
            if not (map[pos - 1] == u'\u2550'.encode('utf-8') \
                or map[pos - 1] == u'\u2551'.encode('utf-8') \
                or map[pos - 1] == u'\u2554'.encode('utf-8') \
                or map[pos - 1] == u'\u255D'.encode('utf-8') \
                or map[pos - 1] == u'\u2557'.encode('utf-8') \
                or map[pos - 1] == u'\u255A'.encode('utf-8') \
                or map[pos - 1] == 'S' \
                or map[pos - 1] == 'B' \
                or map[pos - 1] == ' '):
                player[0] -= 1

        pos = utils.getPosInList(player[0], player[1])
        if map[pos] == u'\u25E2'.encode('utf-8'):
            win.clear()
            run(win, map, stdscr)
            break
        if map[pos] == '*':
            map[pos] = '.'
            player[2] += 10
        elif map[pos] == u'\u2667'.encode('utf-8'):
            map[pos] = '.'
            if (player[3] + 10 > player[4]):
                player[3] = player[4]
            else:
                player[3] += 10
        win.clear()
        win = display.addMapToWin(map, win)
        win = display.addStatsToWin(win, player)
        win.addstr(player[1], player[0], display.player, curses.color_pair(1))
        win.refresh()
        c = stdscr.getch()

def main():
    stdscr = display.initCurses()
    win = curses.newwin(display.SCR_SIZE_Y, display.SCR_SIZE_X)
    run(win, map, stdscr)

    curses.nocbreak()
    stdscr.keypad(0)
    curses.echo()

if __name__ == "__main__":
    main()
