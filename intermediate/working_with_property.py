# working_with_property.py
class Box:
  def __init__(self, weight):
    self.__weight = weight

  def getWeight(self):
    return self.__weight
 
  def setWeight(self, weight):
    if weight >= 0:
      self.__weight = weight

  def delWeight(self):
    del self.__weight

  weight = property(getWeight, setWeight, delWeight, "Docstring for the 'weight' property")


box = Box(10)
box.weight = -5 #box.__weight is unchanged
print(box.weight) #this calls .getWeight()

box.weight = 5 #this called .setWeight()
print(box.weight)

del box.weight #this calls .delWeight()

print(box.weight)
 
