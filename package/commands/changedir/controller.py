import sys
import curses

from ...settings import settings
tty = settings.stdscr
print = settings._print

def run(command = []):
  try:
    if command[0].lower() == 'clear' or command[0].lower() == 'cls':
      tty.clear()
      curses.flushinp()
    elif command[0].lower() == 'exit' and len(command) == 1:
      sys.exit()
    else:
      raise SyntaxError('Invalid Command\n')
  except SyntaxError as error:
    print(error.args[0], curses.color_pair(1))
  except Exception as e:
    if type(e) is SystemExit:
      raise
    else:
      print('Invalid Syntax\n', curses.color_pair(1))