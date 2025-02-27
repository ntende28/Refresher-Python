# def outer_function():
#   enclosing_value = 'Enclosing Value'
 
#   def nested_function():
#     nested_value = 'Nested Value'
#     print(enclosing_value)
  
#   nested_function()

# outer_function()

'''
Flow of scope is upwards, thus the deepest level has access to variables defined
in every enclosing scope above it, but the higher levels don't have access to values
in the lower scopes

'''
# def outer_function():
#   enclosing_value = 'Enclosing Value'
#   print(nested_value)
 
#   def nested_function():
#     nested_value = 'Nested Value'

#     def second_nested():
#        print(enclosing_value)
#        print(nested_value)

#     second_nested() 
  
#   nested_function()

# outer_function()


'''
Values in enclosing scope can be accessed but maynot be changed in the lower scopes!
'''
# def outer_function():
#   enclosing_value = 'Enclosing Value'
  
#   def nested_function():
#     enclosing_value += 'changed'
  
#   nested_function()
#   print(enclosing_value)

# outer_function()


'''
To modify values in the enclosing scope from a deeper level within the enclosing scope
Python provides the nonlocal keyword
'''
def enclosing_function():
  var = "value"

  def nested_function():
    nonlocal var
    var = "new_value"

  nested_function()
  print(var)

enclosing_function()

# global scope variable: by default you cannot change the value of a global variable from within a 
# local scope or function
# gravity = 9.8

# def get_force(mass):
#   gravity += 100
#   return mass * gravity

# print(get_force(60))


'''
Similar to nonlocal, python provides a way to modify global variables from within a function i.e. its local
scope. This maybe achieved by using the global keyword. The global keyword may also be used to define a variable 
to be stored in the global scope if it doesn't exist!
'''

global_var = 10

def some_function():
  global global_var
  global_var = 20

some_function()

print(global_var)
print("\n")

# using global to push a local variable in a function to the global scope
def print_available(color):
  global paint_gallons_available
  paint_gallons_available = {
    'red': 50,
    'blue': 72,
    'green': 99,
    'yellow': 33
  }
  print('There are ' + str(paint_gallons_available[color]) + ' gallons available of ' + color + ' paint.')


print_available('red')
for color in paint_gallons_available:
  print(color)  


'''
Scope resolution is a term used to describe a search procedure for a name in the various namespaces. 
LEGB rule; - Local, Enclosing, Global, Built-in. These four letters represent the order of namespaces
Python will check to see if a name exists. 
'''
age = 27 

def func(): 
  age = 42

  def inner_func():
    print(age)
  
  inner_func() 

func()
