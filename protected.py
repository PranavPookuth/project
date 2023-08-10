class myclass:
    def __init__(self,name,age,address):
        self._Name=name
        self._Address=address
        self.Age=age
    def displayage(self):
        print("Age = ",self.Age)
class child(myclass):
    def myfunction(self):
        print("address is")
obj = myclass("Arya",28,"aaa")
print("Name =",obj._Name)
print("address =",obj._Address)
obj.displayage()
obj2=child("SURTHY",22,"KOCHI")
obj2.myfunction()