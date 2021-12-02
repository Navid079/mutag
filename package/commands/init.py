import os
import shutil
import curses

from ..settings import settings
tty = settings.stdscr
print = tty.addstr

def init():
  print('Initializing mutag...\n')
  try:
    os.mkdir(settings.mutag)
  except:
    raise SyntaxError('Mutag already initialized\nTry <mutag reset> to reinitialize mutag\n')
  print('Done\n')

def reset():
  print("Are you sure you want to reset mutag?[y/N] ")
  curses.flushinp()
  response = tty.getkey()
  if response != 'y': 
    print('Aborted')
    return
  print('\nReseting mutag...\n')
  shutil.rmtree(settings.mutag, ignore_errors=True)
  init()