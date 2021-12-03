import os
import shutil
import curses

from ..settings import settings
tty = settings.stdscr
print = tty.addstr

def init():
  print('Initializing mutag...\n', curses.color_pair(2))
  try:
    os.mkdir(settings.mutag)
  except:
    raise SyntaxError('Mutag already initialized\nTry reset to reinitialize mutag\n')
  print('Done\n', curses.color_pair(2))

def reset():
  print("Are you sure you want to reset mutag?[y/N] ", curses.color_pair(4))
  curses.flushinp()
  response = tty.getkey()
  if response != 'y': 
    print('Aborted\n', curses.color_pair(2))
    return
  print('\nReseting mutag...\n', curses.color_pair(2))
  shutil.rmtree(settings.mutag, ignore_errors=True)
  init()