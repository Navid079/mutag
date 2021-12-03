import os
import sys
import curses
from mutagen.easyid3 import EasyID3

from ...settings import settings
cwd = settings.cwd
mutag = settings.mutag
tty = settings.stdscr
print = settings._print

file = ''

def run(fileName, command = []):
  global file
  file = fileName
  try:
    if command[0].lower() == 'title':
      changeTag('title', ' '.join(command[1:]))
    elif command[0].lower() == 'artist':
      changeTag('artist', ' '.join(command[1:]))
    elif command[0].lower() == 'album':
      changeTag('album', ' '.join(command[1:]))
    elif command[0].lower() == 'clear' or command[0].lower() == 'cls':
      tty.clear()
      curses.flushinp()
    elif command[0].lower() == 'exit' and len(command) == 1:
      sys.exit()
    else:
      raise SyntaxError('Invalid Commands\n')
  except SyntaxError as error:
    print(error.args[0], curses.color_pair(1))
  except Exception as e:
    if type(e) is SystemExit:
      raise
    else:
      print('Invalid Syntax\n', curses.color_pair(1))

def changeTag(tag, value):
  global file
  filePath = os.path.join(cwd, file + '.mp3')
  music = EasyID3(filePath)
  oldValue = music[tag]
  music[tag] = value
  music.save()
  print('Tag changed successfully!\n', curses.color_pair(2))
  print(f'[{tag.capitalize()}] ', curses.color_pair(4))
  print(', '.join(oldValue), curses.color_pair(1))
  print(' --> ')
  print(f'{value}\n', curses.color_pair(3))
  curses.flushinp()