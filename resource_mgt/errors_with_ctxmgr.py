from contextlib import contextmanager

@contextmanager
def open_file_contextlib(file, mode):
  open_file = open(file, mode)

  try:
    yield open_file

  # Exception Handling
  except Exception as exception:
    print('We hit an error: ' + str(exception))

  finally:
    open_file.close()

with open_file_contextlib('file.txt', 'w') as opened_file:
  opened_file.sign('We just made a context manager using contexlib')
