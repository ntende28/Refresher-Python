# test2.py
def arbitrary_keyword_args(**kwargs):
  print(type(kwargs))
  print(kwargs)
  # See if there's an 'anything_goes' keyword arg and print it
  print(kwargs.get('anything_goes'))

arbitrary_keyword_args(this_arg='wowzers', anything_goes=101)


def print_data(**data):
  for arg in data.values():
    print(arg)

print_data(a='arg1', b=True, c=100)


print("------------testing creation of args, kwargs-------------\n")
def print_animals(animal1, animal2, *args, animal4, **kwargs):
  print(animal1, animal2)
  print(args)
  print(animal4)
  print(kwargs)


print_animals('Snake', 'Fish', 'Guinea Pig', 'Owl', animal4='Cat', animal5='Dog')

print("------------Function unpacking-------------\n")

my_num_list = [3, 6, 9]
numbers  = {'num1': 3, 'num2': 6, 'num3': 9}

def sum(num1, num2, num3):
  print(num1 + num2 + num3)

print(my_num_list)
sum(*my_num_list)

print(numbers)
sum(**numbers)

print("------------Combining unpacking and packing-------------\n")

num_collection = [3, 6, 9]

def power_two(*nums): 
  for num in nums:
    print(num**2)

power_two(*num_collection)
