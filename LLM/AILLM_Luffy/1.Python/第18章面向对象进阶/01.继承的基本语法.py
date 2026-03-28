class Animal():
    def eat(self):
        print("eating...")

    def sleep(self):
        print("sleep...")

class Dog(Animal):
    def swimming(self):
        print("swimming...")

class Cat(Animal):
    def climb_tree(self):
        print("climbing_tree...")
        
class Bird(Animal):
    def fly(self):
        print("flying...")
        
alex = Dog()
alex.swimming()
alex.eat()
alex.sleep()