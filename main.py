class Cat:
    def __init__(self,name,age):
        self.name = name
        self.age=age
    def info (self):
        print (f"My name is a Cat {self.name} , I am {self.age} years old")
    def sound (self):
        print ("meow")
class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age=age
    def info (self):
        print (f"My name is a Dog {self.name} , I am {self.age} years old")
    def sound (self):
        print ("bark")

Cat1 = Cat ("Minu" , 12)
dog1 = Dog ("Tommy", 11)

for Animal in (Cat1,dog1):
    Animal.sound()
    Animal.info()
    

class Computer:
    def __init__(self):
        self.__maxprice = 900
    def sell(self):
        print("SellingPrice: {}".format(self.__maxprice))
    def setMaxPrice(self,price):
        self.__maxprice = price

c = Computer()
c.sell()

c.__maxprice = 1000
c.sell()

c.setMaxPrice(1000)
c.sell()