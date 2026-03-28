class Animal():
    def eat(self):
        print("eating...")

    def sleep(self):
        print("self:::", id(self))
        print("sleep...")
        
class Dog(Animal):
    def swimming(self):
        print("swimming...")
        
class Fly(object):
    def fly(self):
        print("flying...")

class Eagle(Animal):
    pass
        

class Bat(Animal):
    pass

b1 = Bat()
b1.fly()

e1 = Eagle()
e1.fly()