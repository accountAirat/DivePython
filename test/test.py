from curses import wrapper

def main(stdscr):
    # Очистить экран
    stdscr.clear()

    # вызывает ZeroDivisionError когда i == 10.
    for i in range(0, 11):
        v = i-10
        stdscr.addstr(i, 0, '10 divided by {} is {}'.format(v, 10/v))

    stdscr.refresh()
    # stdscr.getkey()

wrapper(main)