import curses

from package.settings import settings
settings.init()
from package.commands.controller import run

while 1:
  try:
    curses.flushinp()
    settings.stdscr.addstr('> ', curses.color_pair(1))
    curses.echo()
    command = settings.stdscr.getstr().decode()
    curses.noecho()
    command = command.split(' ')
    run(command)
  except KeyboardInterrupt:
    settings.stdscr.addstr('Use ')
    settings.stdscr.addstr('exit ', curses.color_pair(1))
    settings.stdscr.addstr('to exit\n')
  except SystemExit:
    message = 'Exited'
    break
  except:
    message = 'Failed'
    break
    
settings.end()
print(message)