'''
A context manager is an object that takes care of the assigning and releasing of 
resources (files, database connections, etc). Benefits;
	- Prevent resource leaks
	- Prevent crashes
	-Decrease vulnerability of data
	- Prevent programs from slowing down
'''

# using with as a context manager to open and close a file
# Here the file is automatically closed after script completion
with open("file_name.txt", "w") as file:
   file.write("How you gonna win when you ain't right within?\n")

with open('file_name.txt', 'r') as open_file:
  print(open_file.read())
