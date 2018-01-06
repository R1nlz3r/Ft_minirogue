import curses
import mapGenerator
import display

def main():
    stdscr = display.initCurses()

    map = mapGenerator.initMap()

    win = curses.newwin(display.SCR_SIZE_Y, display.SCR_SIZE_X)

    player_x = 0
    player_y = 0


    win.addch(player_y, player_x, '@', curses.color_pair(1))
    win.refresh()
    while True:
        c = stdscr.getch()
        if c == 27:
            break
        if c == curses.KEY_DOWN and player_y < display.SCR_SIZE_Y - 2:
            player_y += 1
        if c == curses.KEY_UP and player_y > 0:
            player_y -= 1
        if c == curses.KEY_RIGHT and player_x < display.SCR_SIZE_X - 2:
            player_x += 1
        if c == curses.KEY_LEFT and player_x > 0:
            player_x -= 1
        win.clear()
        win = display.addMapToWin(map, win)
        win.addch(player_y, player_x, '@', curses.color_pair(1))
        win.refresh()

    curses.nocbreak()
    stdscr.keypad(0)
    curses.echo()

if __name__ == "__main__":
    main()
