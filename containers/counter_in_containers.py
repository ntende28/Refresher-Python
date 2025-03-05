'''
The Counter container instantly counts elements for any hashable object. It stores the 
data as a dictionary where the keys are the elements and the values are the number
of occurrences
'''
from collections import Counter

clothes_list = ['skirt', 'hoodie', 'dress', 'blouse', 'jeans', 'shoes', 'skirt', 'skirt', 
				'jeans', 'hoodie', 'boots', 'jeans', 'jacket', 't-shirt', 'skirt', 'skirt', 
				'dress', 'shoes', 'blouse', 'hoodie', 'skirt', 'boots', 'shoes', 'boots', 
				'jeans', 'hoodie', 'blouse', 'hoodie', 'shoes', 'shoes', 'blouse', 'boots',
				'blouse', 'hoodie', 't-shirt', 'jeans', 'dress', 'skirt', 'jacket', 'boots', 
				'skirt', 'dress', 'jeans', 'jeans', 'jacket', 'jeans', 'shoes', 'dress', 
				'hoodie', 'blouse']
				
counted_items = Counter(clothes_list)
print(counted_items)