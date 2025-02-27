# abstract_classes.py
from abc import ABC, abstractmethod

class Employee(ABC):  # Abstract class
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @abstractmethod
    def calculate_bonus(self):
        """This method must be implemented in subclasses"""
        pass

# Concrete subclass
class Manager(Employee):
    def calculate_bonus(self):
        return self.salary * 0.10  # 10% bonus

class Developer(Employee):
    def calculate_bonus(self):
        return self.salary * 0.05  # 5% bonus

# Attempting to instantiate Employee will raise an error
# e = Employee("John", 5000)  # TypeError: Can't instantiate abstract class

# Instantiate subclasses
m = Manager("Alice", 8000)
d = Developer("Bob", 6000)

print(m.calculate_bonus())  # Output: 800.0
print(d.calculate_bonus())  # Output: 300.0
