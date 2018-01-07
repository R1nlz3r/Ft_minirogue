import curses
import mapGenerator
import display
import locale
import utils

locale.setlocale(locale.LC_ALL, '')

def run(win, map, stdscr):
    player = utils.getFirstStartingPos(map)

    c = 0
    while True:
        pos = utils.getPosInList(player.pos_x, player.pos_y)
        if c == 27:
            win.clear()
            win.refresh()
            break
        if c == curses.KEY_DOWN and player.pos_y < display.SCR_SIZE_Y - 2:
            if not (map[pos + display.SCR_SIZE_X] == u'\u2550'.encode('utf-8') \
                or map[pos + display.SCR_SIZE_X] == u'\u2551'.encode('utf-8') \
                or map[pos + display.SCR_SIZE_X] == u'\u2554'.encode('utf-8') \
                or map[pos + display.SCR_SIZE_X] == u'\u255D'.encode('utf-8') \
                or map[pos + display.SCR_SIZE_X] == u'\u2557'.encode('utf-8') \
                or map[pos + display.SCR_SIZE_X] == u'\u255A'.encode('utf-8') \
                or map[pos + display.SCR_SIZE_X] == 'S' \
                or map[pos + display.SCR_SIZE_X] == 'B' \
                or map[pos + display.SCR_SIZE_X] == ' '):
                player.pos_y += 1
        if c == curses.KEY_UP and player.pos_y > 0:
            if not (map[pos - display.SCR_SIZE_X] == u'\u2550'.encode('utf-8') \
                or map[pos - display.SCR_SIZE_X] == u'\u2551'.encode('utf-8') \
                or map[pos - display.SCR_SIZE_X] == u'\u2554'.encode('utf-8') \
                or map[pos - display.SCR_SIZE_X] == u'\u255D'.encode('utf-8') \
                or map[pos - display.SCR_SIZE_X] == u'\u2557'.encode('utf-8') \
                or map[pos - display.SCR_SIZE_X] == u'\u255A'.encode('utf-8') \
                or map[pos - display.SCR_SIZE_X] == 'S' \
                or map[pos - display.SCR_SIZE_X] == 'B' \
                or map[pos - display.SCR_SIZE_X] == ' '):
                player.pos_y -= 1
        if c == curses.KEY_RIGHT and player.pos_x < display.SCR_SIZE_X - 2:
            if not (map[pos + 1] == u'\u2550'.encode('utf-8') \
                or map[pos + 1] == u'\u2551'.encode('utf-8') \
                or map[pos + 1] == u'\u2554'.encode('utf-8') \
                or map[pos + 1] == u'\u255D'.encode('utf-8') \
                or map[pos + 1] == u'\u2557'.encode('utf-8') \
                or map[pos + 1] == u'\u255A'.encode('utf-8') \
                or map[pos + 1] == 'S' \
                or map[pos + 1] == 'B' \
                or map[pos + 1] == ' '):
                player.pos_x += 1
        if c == curses.KEY_LEFT and player.pos_x > 0:
            if not (map[pos - 1] == u'\u2550'.encode('utf-8') \
                or map[pos - 1] == u'\u2551'.encode('utf-8') \
                or map[pos - 1] == u'\u2554'.encode('utf-8') \
                or map[pos - 1] == u'\u255D'.encode('utf-8') \
                or map[pos - 1] == u'\u2557'.encode('utf-8') \
                or map[pos - 1] == u'\u255A'.encode('utf-8') \
                or map[pos - 1] == 'S' \
                or map[pos - 1] == 'B' \
                or map[pos - 1] == ' '):
                player.pos_x -= 1

        pos = utils.getPosInList(player.pos_x, player.pos_y)
        if map[pos] == '*':
            map[pos] = '.'
            player.gold += 10
        elif map[pos] == u'\u2667'.encode('utf-8'):
            map[pos] = '.'
            if (player.life + 10 > player[4]):
                player.life = player.maxLife
            else:
                player.life += 10
        win.clear()
        win = display.addMapToWin(map, win)
        win = display.addStatsToWin(win, player)
        win.addstr(player.pos_y, player.pos_x, display.player, curses.color_pair(1))
        win.refresh()
        if (player.life <= 0):
            utils.you_died(curses, win, stdscr, player)
            break
        c = stdscr.getch()

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
