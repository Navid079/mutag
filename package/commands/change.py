import os
import shutil
import curses
import re
from mutagen import easyid3

from .changedir.controller import run
from ..settings import settings

cwd = settings.cwd
mutag = settings.mutag
tty = settings.stdscr
print = settings._print

def change(command = []):
  if command[0].lower() == 'id' and len(command) == 2:
    changeByIdInteractive(command[1])


def changeByIdInteractive(id):
  try:
    id = int(id)
  except:
    raise SyntaxError('Invalid id\n')
  with open(os.path.join(mutag, 'list.txt'), 'r') as lst:
    foundId, foundName = '', ''
    for line in lst:
      search = re.search('^(.*):([0-9]+)$', line)
      foundName = search.group(1)
      foundId = search.group(2)
      foundId = int(foundId)
      if id == foundId:
        break
    if foundId == '' or foundId != id:
      raise SyntaxError('ID not found!\n')
    while 1:
      try:
        curses.flushinp()
        print(f'{foundName}', curses.color_pair(3))
        print(f' > ', curses.color_pair(1))
        curses.echo()
        command = settings.stdscr.getstr().decode()
        curses.noecho()
        command = command.split(' ')
        run(foundName, command)
      except FileNotFoundError as error:
        changeFileName(foundName, error.args[0])
        foundName = error.args[0]
      except KeyboardInterrupt:
        settings.stdscr.addstr('Use ')
        settings.stdscr.addstr('exit ', curses.color_pair(1))
        settings.stdscr.addstr('to exit "interctive change"\n')
      except SystemExit:
        return
      except:
        raise SyntaxError('Failed\n')
  
def changeFileName(name, newName):
  with open(os.path.join(mutag, 'tmplist.txt'), 'w') as newLst:
    with open(os.path.join(mutag, 'list.txt'), 'r') as lst:
      for line in lst:
        search = re.search('^(.*):([0-9]+)$', line)
        foundName = search.group(1)
        foundId = search.group(2)
        if foundName == name:
          newLst.write(f'{newName}:{foundId}\n')
        else:
          newLst.write(line)
  os.rename(os.path.join(cwd, name + '.mp3'), newName + '.mp3')
  os.remove(os.path.join(mutag, 'list.txt'))
  os.rename(os.path.join(mutag, 'tmplist.txt'), os.path.join(mutag, 'list.txt'))
  print('Name changed successfully!\n', curses.color_pair(2))
  