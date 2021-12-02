import os
import re

cwd = os.getcwd()
files = filter(lambda f: re.match(r'.*\.mp3|.*\.Mp3|.*\.mP3|.*\.MP3', f), os.listdir(cwd))

def create(command = []):
  try:
    if command[0].lower() == 'list' and len(command) == 1:
      createList()
    else:
      raise Exception()
  except:
      raise SyntaxError('Invalid Command - See create -h for help')

def createList():
  print('Creating List...')
  print(f'Working Directory: {cwd}')
  print(f'Listing Files:')
  for file in files:
    print(f'{file} found')