class myclass:
    def __init__(self,name,age):
        self.Name=name
        self.Age=age
    def displayage(self):
        print("Age :",self.Age)
        print("name :",self.Name)

obj=myclass("Arya ", 28)
obj.displayage()