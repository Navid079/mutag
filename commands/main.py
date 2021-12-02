from .create import create

def run(command = []):
  try:
    if command[0].lower() == 'create':
      create(command[1:])
    else:
      raise SyntaxError('Invalid Command')
  except SyntaxError as error:
    print(error.args[0])
  except:
    print('Invalid Syntax')