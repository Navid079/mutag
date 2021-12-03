import os
import curses

from ..settings import settings

cwd = settings.cwd
mutag = settings.mutag
tty = settings.stdscr
print = settings._print

def Print(command = []):
  try:
    if command[0].lower() == 'list' and len(command) == 1:
      printList()
    else:
          raise Exception()
  except:
      raise SyntaxError('Invalid Command - See print -h for help\n')


def printList():
  print('Printing list...\n', curses.color_pair(2))
  with open(os.path.join(mutag, 'list.txt'), 'r') as lst:
    for line in lst:
      name, id = line.split(':')
      print(str(name), curses.color_pair(3))
      print(':')
      print(f'{str(id)}\n', curses.color_pair(2))