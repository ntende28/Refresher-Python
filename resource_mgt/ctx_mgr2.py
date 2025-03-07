# ctx_mgr2.py
class OpenFile:
 
 def __init__(self, file, mode):
   self.file = file
   self.mode = mode

 def __enter__(self):
   self.opened_file = open(self.file, self.mode)
   return self.opened_file
 
 def __exit__(self, exc_type, exc_val, traceback):
   print(exc_type)
   print(exc_val)
   print(traceback)
   self.opened_file.close()

with OpenFile("file_name.txt", "r") as file:
  # .see() is not a real method
  print(file.read())
