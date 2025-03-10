# example2.py
class WorkWithFile:
  def __init__(self, file, mode):
    self.file = file
    self.mode = mode
 
  def __enter__(self):
    self.opened_file = open(self.file, self.mode)
    return self.opened_file
 
  def __exit__(self, *exc):
    self.opened_file.close()

with WorkWithFile('file_name.txt', 'r') as file:
	print(file.read())
