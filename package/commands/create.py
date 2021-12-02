import os
import re

from ..settings import settings

cwd = settings.cwd
mutag = settings.mutag
tty = settings.stdscr
print = settings._print

files = filter(lambda f: re.match(r'.*\.mp3|.*\.Mp3|.*\.mP3|.*\.MP3', f), os.listdir(cwd))

def create(command = []):
  try:
    if command[0].lower() == 'list' and len(command) == 1:
      createList()
    else:
      raise Exception()
  except:
      raise SyntaxError('Invalid Command - See create -h for help\n')

def createList():
  print('Creating List...\n')
  print(f'Working Directory: {cwd}\n')
  print(f'Listing Files:\n')
  with open(os.path.join(mutag, 'list.txt'), 'w') as lst:
    for i, file in enumerate(files):
      print(f'{file} found\n')
      lst.write(f'{file}:{i}')