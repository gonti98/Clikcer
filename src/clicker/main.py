import curses
from curses import wrapper

def app(stdscr) -> None:
    stdscr.clear()
    stdscr.addstr(0, 0, ".")
    stdscr.refresh()
    stdscr.getch()

def main():
    curses.wrapper(app)
