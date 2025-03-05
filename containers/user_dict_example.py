from collections import UserDict

# Create a class which inherits from the UserDict class
class DisplayDict(UserDict):
    # A new method to increase the dictionary's functionality
    def display_info(self):
        print("Number of Keys: " + str(len(self.keys())))
        print("Keys: " + str(list(self.keys())))
        print("Number of Values: " + str(len(self.values())))
        print("Values: " + str(list(self.values())))

    # We can also overwrite a method from the dictionary class
    def clear(self):
        print("Deleting all items from the dictionary!")
        super().clear()

disp_dict = DisplayDict({'user': 'Mark', 'device': 'desktop', 'num_visits': 37})

disp_dict.display_info()

disp_dict.clear()
