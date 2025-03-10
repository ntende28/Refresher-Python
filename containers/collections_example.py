from collections import deque, namedtuple

overstock_items = [['shirt_103985', 15.99],
                    ['pants_906841', 19.99],
                    ['pants_765321', 15.99],
                    ['shoes_948059', 29.99],
                    ['shoes_356864', 9.99],
                    ['shirt_865327', 10.99],
                    ['shorts_086853', 9.99],
                    ['pants_267953', 21.99],
                    ['dress_976264', 32.99],
                    ['shoes_135786', 17.99],
                    ['skirt_196543', 12.99],
                    ['jacket_976535', 26.99],
                    ['pants_086367', 30.99],
                    ['dress_357896', 29.99],
                    ['shoes_157895', 14.99]]

# Write your code below!
split_prices = deque()

for item in overstock_items:
  if item[1] >= 20:
    split_prices.appendleft(item)
  else:
    split_prices.append(item)

print("The split_prices deque collection: ")
print(split_prices)
print("\n")

ClothesBundle = namedtuple('ClothesBundle', ['bundle_items', 'bundle_price'])
bundles = []
while len(split_prices) >= 5:
  bundle_list = [split_prices.pop(), split_prices.pop(), split_prices.pop(), split_prices.popleft(), split_prices.popleft()]
  calc_price = sum(b[1] for b in bundle_list)
  bundles.append(ClothesBundle(bundle_list, calc_price))

print("The bundles list containing namedtuples of ClothesBundle: ")
print(bundles)
print("\n")

promoted_bundles = [bundle for bundle in bundles if bundle.bundle_price > 100]
print("The bundles to be promoted i.e. having a price > 100: ")
print(promoted_bundles)