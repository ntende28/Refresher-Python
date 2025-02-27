# functions as objects
def add_five(num):
	print(num + 5)

print("Functions as objects")
print(add_five)
print("\n")

# functions within functions
def add_num(num):
	def add_two(num):
		return num + 2

	num_plus_two = add_two(num)
	print(num_plus_two + 3)

print("Functions within Functions")
# add_two(2) - only defined in the scope of add_num
add_num(20)
print("\n")

# returning functions from functions
def get_math_function(operation): #returns + or - operation
	def add(n1, n2): 
		return n1 + n2

	def sub(n1, n2):
		return n1 - n2

	if operation == '+':
		return add
	elif operation == '-':
		return sub

print("Returning a function from a function")
add_function = get_math_function('+')
sub_function = get_math_function('-')
print(sub_function(12, 12))	
print("\n")

'''
Decorating a function - A decorator is a function that takes in a function and
executes the function together with some extra logic.

Each decorator contains a wrapper function, which is returned by the decorator function
'''
def title_decorator(print_name_fn):
	def wrapper(*args, **kwargs):
		print("Engineering Consultant : ")
		print_name_fn(*args, **kwargs)
	return wrapper

# @title_decorator # - using the python in-built decorator
def print_my_name():
	print("Kenn")

@title_decorator # - using the python in-built decorator
def print_mover(company_name, description, age):
	print(company_name + " is a "+ description + " with "+ str(age) + " years of experience")

# decorated_fn = title_decorator(print_my_name)
# decorated_fn()
print("Decorating a function")
print_my_name()
print_mover("MoveRobotic Sdn Bhd", "Robotics, Engineering, Design company", 6)


'''
Decorators with a function

'''