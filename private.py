# program to illustrate private access modifier in a class

class Geek:
    # private members
    __name = None
    __roll = None
    __branch = None
    def __init__(self, name, roll, branch):
        self.__name = name
        self.__roll = roll
        self.__branch = branch

    # private member function
    def __displayDetails(self):
        # accessing private data members
        print("Name: ", self.__name)
        print("Roll: ", self.__roll)
        print("Branch: ", self.__branch)

    def accessPrivateFunction(self):
        # accessing private member function
        self.__displayDetails()
obj = Geek("pranav", 36, "phyton")
obj.accessPrivateFunction()
