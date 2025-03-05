from collections import ChainMap

customer_info = {'name': 'Dmitri Buyer', 'age': '31', 'address': '123 Python Lane', 'phone_number': '5552930183'}

shirt_dimensions = {'shoulder': 20, 'chest': 42, 'torso_length': 29}

pants_dimensions = {'waist': 36, 'leg_length': 42.5, 'hip': 21.5, 'thigh': 25, 'bottom': 18}

# creating an instance of chainmap
customer_data = ChainMap(customer_info, shirt_dimensions, pants_dimensions)
print(customer_data)
print('\n')

customer_leg_length = customer_data['leg_length']
print("The customer's leg length is " + str(customer_leg_length))
print('\n')

'''
The parents property skips the first mapping and returns everything else (all of the parents of the first mapping).
'''
customer_size_data = customer_data.parents
print(f"Parents as returned by ChainMap : {customer_size_data}")
print('\n')

customer_data['address'] = '456 ChainMap Drive'
print("after modifying address")
print(customer_data)


'''
ChainMap(*my_list) - Allows for the my_list variable to be expanded into separate variables instead of a single
variable
'''