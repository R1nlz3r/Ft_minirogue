import curses
import mapGenerator
import display
import locale
import utils
import random

import time

locale.setlocale(locale.LC_ALL, '')

def run(win, map, stdscr, player):
    map = mapGenerator.initMap()
    player = utils.getFirstStartingPos(map, player)
    monsters = [utils.monster(0)] * 20
    nbMonsters = random.randint(3, 10)
    for i in range(20):
        monsters[i] = utils.monster(i)
    for i in range(nbMonsters):
        pos_monster = utils.getRandomDot(map)
        monsters[i].pos_x = pos_monster[0]
        monsters[i].pos_y = pos_monster[1]
        type = random.randint(1, 4)
        if (type == 1):
            monsters[i].type = utils.BAT
            monsters[i].life = 6
            monsters[i].attack = 3
        else:
            monsters[i].type = utils.SNAKE
            monsters[i].life = 5
            monsters[i].attack = 2

    win.clear()
    win = display.addMapToWin(map, win)
    win = display.addStatsToWin(win, player)
    win.addstr(player.pos_y, player.pos_x, display.player, curses.color_pair(1))
    for i in range(20):
        if not (monsters[i].type == 'A'):
            win.addstr(monsters[i].pos_y, monsters[i].pos_x, monsters[i].type, curses.color_pair(0))
    win.refresh()

    time.sleep(1)
    c = stdscr.getch()
    while True:
        pos = utils.getPosInList(player.pos_x, player.pos_y)


        if c == 27:
            win.clear()
            win.refresh()
            break

        if (utils.is_monster(pos + display.SCR_SIZE_X, monsters)):
            monster_id = utils.which_monster(pos + display.SCR_SIZE_X, monsters)
            player.life -= random.randint(0, monsters[monster_id].attack)
        if (utils.is_monster(pos - display.SCR_SIZE_X, monsters)):
            monster_id = utils.which_monster(pos - display.SCR_SIZE_X, monsters)
            player.life -= random.randint(0, monsters[monster_id].attack)
        if (utils.is_monster(pos + 1, monsters)):
            monster_id = utils.which_monster(pos + 1, monsters)
            player.life -= random.randint(0, monsters[monster_id].attack)
        if (utils.is_monster(pos - 1, monsters)):
            monster_id = utils.which_monster(pos - 1, monsters)
            player.life -= random.randint(0, monsters[monster_id].attack)

        if c == curses.KEY_DOWN and player.pos_y < display.SCR_SIZE_Y - 2:
            if not (map[pos + display.SCR_SIZE_X] == u'\u2550'.encode('utf-8') \
                or map[pos + display.SCR_SIZE_X] == u'\u2551'.encode('utf-8') \
                or map[pos + display.SCR_SIZE_X] == u'\u2554'.encode('utf-8') \
                or map[pos + display.SCR_SIZE_X] == u'\u255D'.encode('utf-8') \
                or map[pos + display.SCR_SIZE_X] == u'\u2557'.encode('utf-8') \
                or map[pos + display.SCR_SIZE_X] == u'\u255A'.encode('utf-8') \
                or map[pos + display.SCR_SIZE_X] == ' '):
                if not utils.is_monster(pos + display.SCR_SIZE_X, monsters):
                    player.pos_y += 1
                else:
                    monster_id = utils.which_monster(pos + display.SCR_SIZE_X, monsters)
                    monsters[monster_id].life -= random.randint(0, player.attack)
                    if (monsters[monster_id].life <= 0):
                        monsters[monster_id].type = 'A'
                        player.gold += 30
                        player.kill += 1
        if c == curses.KEY_UP and player.pos_y > 0:
            if not (map[pos - display.SCR_SIZE_X] == u'\u2550'.encode('utf-8') \
                or map[pos - display.SCR_SIZE_X] == u'\u2551'.encode('utf-8') \
                or map[pos - display.SCR_SIZE_X] == u'\u2554'.encode('utf-8') \
                or map[pos - display.SCR_SIZE_X] == u'\u255D'.encode('utf-8') \
                or map[pos - display.SCR_SIZE_X] == u'\u2557'.encode('utf-8') \
                or map[pos - display.SCR_SIZE_X] == u'\u255A'.encode('utf-8') \
                or map[pos - display.SCR_SIZE_X] == ' '):
                if not utils.is_monster(pos - display.SCR_SIZE_X, monsters):
                    player.pos_y -= 1
                else:
                    monster_id = utils.which_monster(pos - display.SCR_SIZE_X, monsters)
                    monsters[monster_id].life -= random.randint(0, player.attack)
                    if (monsters[monster_id].life <= 0):
                        monsters[monster_id].type = 'A'
                        player.gold += 30
                        player.kill += 1
        if c == curses.KEY_RIGHT and player.pos_x < display.SCR_SIZE_X - 2:
            if not (map[pos + 1] == u'\u2550'.encode('utf-8') \
                or map[pos + 1] == u'\u2551'.encode('utf-8') \
                or map[pos + 1] == u'\u2554'.encode('utf-8') \
                or map[pos + 1] == u'\u255D'.encode('utf-8') \
                or map[pos + 1] == u'\u2557'.encode('utf-8') \
                or map[pos + 1] == u'\u255A'.encode('utf-8') \
                or map[pos + 1] == ' '):
                if not utils.is_monster(pos + 1, monsters):
                    player.pos_x += 1
                else:
                    monster_id = utils.which_monster(pos + 1, monsters)
                    monsters[monster_id].life -= random.randint(0, player.attack)
                    if (monsters[monster_id].life <= 0):
                        monsters[monster_id].type = 'A'
                        player.gold += 30
                        player.kill += 1
        if c == curses.KEY_LEFT and player.pos_x > 0:
            if not (map[pos - 1] == u'\u2550'.encode('utf-8') \
                or map[pos - 1] == u'\u2551'.encode('utf-8') \
                or map[pos - 1] == u'\u2554'.encode('utf-8') \
                or map[pos - 1] == u'\u255D'.encode('utf-8') \
                or map[pos - 1] == u'\u2557'.encode('utf-8') \
                or map[pos - 1] == u'\u255A'.encode('utf-8') \
                or map[pos - 1] == ' '):
                if not utils.is_monster(pos - 1, monsters):
                    player.pos_x -= 1
                else:
                    monster_id = utils.which_monster(pos - 1, monsters)
                    monsters[monster_id].life -= random.randint(0, player.attack)
                    if (monsters[monster_id].life <= 0):
                        monsters[monster_id].type = 'A'
                        player.gold += 30
                        player.kill += 1
        pos = utils.getPosInList(player.pos_x, player.pos_y)
        if map[pos] == u'\u25E2'.encode('utf-8'):
            win.clear()
            player.level += 1
            run(win, map, stdscr, player)
            break
        if map[pos] == '*':
            map[pos] = '.'
            player.gold += 10
        elif map[pos] == u'\u2667'.encode('utf-8'):
            map[pos] = '.'
            if (player.life + 10 > player.maxLife):
                player.life = player.maxLife
            else:
                player.life += 10
        win.clear()
        win = display.addMapToWin(map, win)
        win = display.addStatsToWin(win, player)
        win.addstr(player.pos_y, player.pos_x, display.player, curses.color_pair(1))
        for i in range(20):
            if not (monsters[i].type == 'A'):
                win.addstr(monsters[i].pos_y, monsters[i].pos_x, monsters[i].type, curses.color_pair(0))
        win.refresh()
        if (player.life <= 0):
            utils.you_died(curses, win, stdscr, player)
            break
        player.turns += 1
        c = stdscr.getch()

def main():
    stdscr = display.initCurses()
    win = curses.newwin(display.SCR_SIZE_Y, display.SCR_SIZE_X)
    playr = utils.player()
    playr.gold = 0
    playr.life = 100
    playr.maxLife = 100
    run(win, map, stdscr, playr)

    curses.nocbreak()
    stdscr.keypad(0)
    curses.echo()

if __name__ == "__main__":
    main()
