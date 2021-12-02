import os
import curses

stdscr = None
_print = None
cwd = ''
mutag = ''

def init():
  global stdscr
  stdscr = curses.initscr()
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