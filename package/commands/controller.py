import sys
import curses

from .init import init, reset
from .create import create
from .print import Print
from ..settings import settings
tty = settings.stdscr
print = settings._print

def run(command = []):
  try:
    if command[0].lower() == 'init' and len(command) == 1:
      init()
    elif command[0].lower() == 'reset' and len(command) == 1:
      reset()
    elif command[0].lower() == 'create':
      create(command[1:])
    elif command[0].lower() == 'print':
      Print(command[1:])
    elif command[0].lower() == 'clear':
      tty.clear()
      curses.flushinp()
    elif command[0].lower() == 'exit' and len(command) == 1:
      sys.exit()
    else:
      raise SyntaxError('Invalid Command\n')
  except SyntaxError as error:
    print(error.args[0])
  except Exception as e:
    if type(e) is SystemExit:
      raise
    else:
      print('Invalid Syntax\n')