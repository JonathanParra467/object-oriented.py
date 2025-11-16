"""
Create the Pet Class:
Define a Pet class with attributes: kind (e.g., dog, cat), breed, and name.
Implement get and set methods for each of these attributes.
Add a method called print_details that prints the details of the pet.
Create Instances:
Create three objects of the Pet class with different kinds, breeds, and names.

Call the print_details method for each object that you created

Demonstrate a Special Method or Function:
Choose three of the following and demonstrate its use with the Pet class instances:

__name__: Display the name of the class.
type(): Show the class used to instantiate a pet object.
__module__: Return the module name in which the Pet class is defined.
__bases__: Display the base classes of the Pet class (if any).
isinstance(): Check if an instance is of the Pet class.
"""


class Pet:

    pet_name = "kendrick"


    def __init__(self, kind, breed, name):

        self.__kind = kind
        self.__breed = breed
        self.__name = name

    def get_kind(self):
        return self.__kind
    
    def get_breed(self):
        return self.__breed
    
    def get_name(self):
        return self.__name
    
    def set_kind(self, value):
        self.__kind = value
        
    def set_breed(self, value):
        self.__breed = value

    def set_name(self, value):
        self.__name = value

    def print_details(self):
        print("pet_details: ", vars(self))
        
    def print_info(self):
        print(self.__kind)
        print(self.__breed)
        print(self.__name)

        print(Pet.__module__)

        print(Pet.__bases__)

        print(Pet.__module__)

def main():

        pet1 = Pet("Bird", "Falcon", "Brandon")
        pet2 = Pet("Cat", "Ragdoll", "Fred")
        pet3 = Pet("Dog", "Poodle", "John")
        
        print("pet details: ")
        print(pet1.get_kind())
        print(pet1.get_breed())
        print(pet1.get_name())

        print("pet details: ")
        print(pet2.get_kind())
        print(pet2.get_breed())
        print(pet2.get_name())

        print("pet details: ")
        print(pet3.get_kind())
        print(pet3.get_breed())
        print(pet3.get_name())

        

main()