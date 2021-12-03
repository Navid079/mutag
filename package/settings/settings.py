import os
import curses

stdscr = None
_print = None
cwd = ''
mutag = ''

def init():
  global stdscr
  stdscr = curses.initscr()
  curses.start_color()
  curses.use_default_colors()
  curses.init_pair(1, curses.COLOR_RED, -1)
  curses.init_pair(2, curses.COLOR_CYAN, -1)
  curses.init_pair(3, curses.COLOR_MAGENTA, -1)
  curses.init_pair(4, curses.COLOR_GREEN, -1)

  curses.cbreak()
  curses.noecho()
  stdscr.keypad(True)
  global _print
  _print = stdscr.addstr
  global cwd
  cwd = os.getcwd()
  global mutag
  mutag = os.path.join(cwd, '.mutag')

def end():
  global stdscr
  curses.nocbreak()
  curses.echo()
  stdscr.keypad(False)
  curses.endwin()