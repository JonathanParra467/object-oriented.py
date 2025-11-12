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
    
    def set_name(self, value):
        self.__kind = value
        
    def set_name(self, value):
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

        pet1 = Pet("bird", "falcon", "brandon")
        pet2 = Pet("kat", "ket", "fred")
        pet3 = Pet("dog", "poodle", "john")

        print(pet1.get_kind())
        print(pet1.get_breed())
        print(pet1.get_name())

        print(pet2.get_kind())
        print(pet2.get_breed())
        print(pet2.get_name())

        print(pet3.get_kind())
        print(pet3.get_breed())
        print(pet3.get_name())

        

main()