from contextlib import contextmanager

@contextmanager
def open_file_contextlib(file, mode):
  opened_file = open(file, mode)
 
  try:
    yield opened_file

  finally:
    opened_file.close()

with open_file_contextlib('file.txt', 'w') as opened_file:
  opened_file.write('We just made a context manager using contexlib')
