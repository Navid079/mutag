import curses

from package.settings import settings
settings.init()
from package.commands.controller import run

while 1:
  try:
    settings.stdscr.addstr('> ')
    curses.echo()
    command = settings.stdscr.getstr().decode()
    curses.noecho()
    command = command.split(' ')
    run(command)
  except KeyboardInterrupt:
    curses.flushinp()
    pass
  except SystemExit:
    message = 'Exited'
    break
  except:
    message = 'Failed'
    break
    
settings.end()
print(message)