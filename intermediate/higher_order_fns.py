# higher_order_fns.py

'''
In Python, all functions, including the ones we’ve written, are classified as first-class objects
This implies that;
	
    1. First-class objects can be stored as variables.
    2. First-class objects can be passed as arguments to a function.
    3. First-class objects can be returned by a function.
    4. First-class objects can be stored in data structures (e.g., lists, dictionaries, etc.).

'''

# Here, we assign a function to a variable
uppercase = str.upper 

# And then call it 
big_pie = uppercase("pumpkinpie")
print(big_pie)

# Here we store two functions in a list
string_manipulation_functions = [str.upper, str.lower] 

# passing a function as an argument i.e. concept of callback functions
def total_bill(func, value):
  total = func(value)
  return ("The total amount owed is $" + "{:.2f}".format(total) + ". Thank you! :)")

# function to be passed as an argument
def add_tax(total):
  tax = total * 0.06
  new_total = total + tax
  return new_total

def add_tip(total):
  tip = total * .2
  new_total = total + tip
  return new_total


# calling the two functions
print(total_bill(add_tip, 100))
print(total_bill(add_tax, 100))
print("\n")

# Functions as arguments - Iteration
bills = [115, 120, 42]
 
# new_bills = []
 
# for i in range(len(bills)):
#   total = add_tax(bills[i])
#   new_bills.append("Total amount owed is $" + "{:.2f}".format(total) + ". Thank you! :)")

# print(new_bills)

def total_bills(func, list):
	# This list will store all the new bill values
	new_bills = []

	# This loop will iterate through our bills
	for i in range(len(list)):
		# Here we apply the function to each element of the list!
		total = func(list[i])
		new_bills.append("Total amount owed is $" + "{:.2f}".format(total) + ". Thank you! :)")

	return new_bills

bills_w_tax = total_bills(add_tax, bills)
bills_w_tip = total_bills(add_tip, bills)

print("Using the same higher-order function for processing taxes")
print(bills_w_tax)
print("\n")

print("Using the same higher-order function for adding tips!")
print(bills_w_tip)
print("\n")



# Functions as return values
print("Using functions as return values")

def make_box_volume_function(height):
    # defines and returns a function that takes two numeric arguments,        
    # length &  width, and returns the volume given the input height
    def volume(length, width):
        return length*width*height

    return volume
 
box_volume_height15 = make_box_volume_function(15)
 
print(box_volume_height15(3,2))