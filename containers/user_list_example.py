from collections import UserList

data = [4, 6, 8, 9, 5, 7, 3, 1, 0]

# Write your code below!
class ListSorter(UserList):
  def append(self, item):
    super().append(item)
    super().sort()

sorted_list = ListSorter(data)
sorted_list.append(2)

print(sorted_list)