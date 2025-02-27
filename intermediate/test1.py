# test1.py - Working with the mutable default arguments
# def createStudent(name, age, grades=[]):
#     return {
#         'name': name,
#         'age': age,
#         'grades': grades
#     }


# def addGrade(student, grade):
#     student['grades'].append(grade)
#     # To help visualize the grades we have added a print statement
#     print(student['grades'])



# chrisley = createStudent('Chrisley', 15)
# dallas = createStudent('Dallas', 16)

# addGrade(chrisley, 90)
# addGrade(dallas, 100)


'''
When we call a function, the default values we provide for parameters are only created once, and used 
for each subsequent call of the function. This means our grades=[] from our earlier function was only 
created once and anytime we tried to access it, the same list was being modified. 
'''

# The ids printed will vary depending on the computer we are using. 
# print(id(chrisley['grades']))
# print(id(dallas['grades']))


# You can work around this using the None keyword
def createStudent(name, age, grades=None):
  if grades is None:
    grades = []

  return {
    'name': name,
    'age': age,
    'grades': grades
  }

def addGrade(student, grade):
    student['grades'].append(grade)
    # To help visualize the grades we have added a print statement
    print(student['grades'])

chrisley = createStudent('Chrisley', 15)
dallas = createStudent('Dallas', 16)

addGrade(chrisley, 90)
addGrade(dallas, 100)