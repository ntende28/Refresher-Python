
'''
Lambda functions are single line functions i.e. anonymous functions that can be used 
as shorthand for creating a function
	-	The lambda keyword declares that this is a lambda function
	-	my_input is a parameter used to hold the value passed to
	-	In the lambda function version, we are returning my_input + 2 without 
	the use of a return keyword
'''

add_two = lambda my_input: my_input + 2

print(add_two(3))
print(add_two(100))
print(add_two(-2))

print("\n")

# conditionals in lambda functions
check_if_A_grade = lambda grade: 'Got an A!' if grade >= 90 else 'Did not get an A.'

print(check_if_A_grade(91))
print(check_if_A_grade(70))
print(check_if_A_grade(20))