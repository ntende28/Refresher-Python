from functools import reduce


def double(x):
 return x*2
 
int_list = [3, 6, 9]
 
# doubled = map(double, int_list)

'''
a map is a built-in function that takes in two arguments i.e. a function and an iterable object
e.g. a list. The map function applies the passed function to each element in the iterable and
returns a map object.
using map with lambdas;

''' 
doubled = map(lambda input: input*2, int_list)
 
print(list(doubled))
print("\n")

grade_list = [3.5, 3.7, 2.6, 95, 87]

# Note: A lambda function does not support an if statement without an else statement
grades_100scale = map(lambda grade: grade*25 if grade <= 4 else grade, grade_list)
# assign the result of your map function to the variable grades_100scale

# convert grades_100scale to a list and save it as updated_grade_list 
updated_grade_list = list(grades_100scale)

# print updated_grade_list
print(updated_grade_list)
print("\n")


'''
filter(func, iterable) - It takes a function and iterable obj, and it filters out select elements from the iterable
based on fulfilling the condition in function. The function passed must return a boolean value i.e. true
or false.
It returns a filter object
'''
names = ["margarita", "Linda", "Masako", "Maki", "Angela"]
 
M_names = filter(lambda name: name[0] == "M" or name[0] == "m", names) 
 
print(list(M_names))
print("\n")

# deduplicate the list and keep only the sublists that have the book title stored as a string
books = [
    ["Burgess", 1985],
    ["Orwell", "Nineteen Eighty-four"],
    ["Murakami", "1Q85"],
    ["Orwell", 1984],
    ["Burgess", "Nineteen Eighty-five"],
    ["Murakami", 1985]
]

'''
Lambda function to filter lists where both elements are strings
- isinstance(object, type) - returns True if the specified object is of the specified type, otherwise False.
'''
filtered_books = list(filter(lambda x: isinstance(x[0], str) and isinstance(x[1], str), books))

print(filtered_books)
print("\n")

'''
reduce() - Has to be imported from the functools library
- It returns a single value, from an iterable passed i.e. to get to this single value, reduce() cumulatively 
applies a passed function to each sequential pair of elements in an iterable.
reduce(func, iterable)
'''
int_list = [3, 6, 9, 12]
 
reduced_int_list = reduce(lambda x,y: x*y, int_list)
 
print(reduced_int_list)
