from collections import defaultdict, namedtuple

site_locations = {'t-shirt': 'Shirts',
                  'dress shirt': 'Shirts',
                  'flannel shirt': 'Shirts',
                  'sweatshirt': 'Shirts',
                  'jeans': 'Pants',
                  'dress pants': 'Pants',
                  'cropped pants': 'Pants',
                  'leggings': 'Pants'
                  }
updated_products = ['draped blouse', 'leggings', 'undershirt', 'dress shirt', 'jeans', 'sun dress', 'flannel shirt', 'cropped pants', 'dress pants', 't-shirt', 'camisole top', 'sweatshirt']

# Write your code below!
validated_locations = defaultdict(lambda: 'TODO: Add to website')
validated_locations.update(site_locations)

for item in updated_products:
  site_locations[item] = validated_locations[item]

print('Default dict example: ')
print(site_locations)
print('\n')

print('Named tuple example')
ActorData = namedtuple('ActorData', ['name', 'birth_year', 'movie', 'movie_release_date'])
actor_data = ActorData('Leonardo DiCarprio', 1974, 'Titanic', 1997)
print(actor_data.name)
print(actor_data.birth_year)
print(actor_data.movie)
print(actor_data.movie_release_date)    