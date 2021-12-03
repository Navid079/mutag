import curses
import os
import re

from ..settings import settings

cwd = settings.cwd
mutag = settings.mutag
tty = settings.stdscr
print = settings._print

files = filter(lambda f: re.match(r'.*\.mp3$', f, re.IGNORECASE), os.listdir(cwd))

def create(command = []):
  try:
    if command[0].lower() == 'list' and len(command) == 1:
      createList()
    else:
      raise Exception()
  except:
      raise SyntaxError('Invalid Command - See create -h for help\n')

def createList():
  print('Creating List...\n', curses.color_pair(2))
  print(f'Listing Files:\n', curses.color_pair(2))
  with open(os.path.join(mutag, 'list.txt'), 'w') as lst:
    for i, file in enumerate(files):
      print(f'{file[:-4]} ', curses.color_pair(3))
      print('found\n', curses.color_pair(2))
      lst.write(f'{file[:-4]}:{i}')