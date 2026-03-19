# # 案例一：
# class Animal():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def eat(self):
#         print("eating...")

#     def sleep(self):
#         print("sleep...")

# class Dog(Animal):
    
#     def __init__(self, name, age, breed):
#         super().__init__(name, age)
#         self.breed = breed
    
#     def swimming(self):
#         print("swimming...")
        
# alex = Dog("alex", 34, "斗牛犬")
# alex.sleep()

# class Cat(Animal):
    
#     def __init__(self, name, age, color):
#         super().__init__(name, age)
#         self.color = color
    
#     def climb_tree(self):
#         print("climbing_tree...")
        
# c1 = Cat("喵喵", 2, "white")
# c1.climb_tree()

# 案例二：
class Base:

    def __init__(self):
        self.func()

    def func(self):
        print('in base')


class Son(Base):
    def func(self):
        print('in son')
    
    # def eat(self):
    #     print('eatting')

s= Son()

