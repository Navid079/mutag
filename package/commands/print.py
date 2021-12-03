
import os
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
  print('Printing list...\n')
  with open(os.path.join(mutag, 'list.txt'), 'r') as lst:
    for line in lst:
      print(f'{line}\n')