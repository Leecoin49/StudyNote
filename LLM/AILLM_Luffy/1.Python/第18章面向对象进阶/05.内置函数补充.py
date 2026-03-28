# class Animal():
#     def eat(self):
#         print("eating...")

#     def sleep(self):
#         print("self:::", id(self))
#         print("sleep...")
        
# class Dog(Animal):
#     def swimming(self):
#         print("swimming...")

# # type和isinstance      
# alex = Dog()
# print(isinstance(alex, Dog))
# print(isinstance(alex, Animal))

# dir函数和__dict__属性
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def test(self):
        pass

alex = Student("alex", 32)
# print(alex.__dict__)

print(dir(alex))
print(alex.__class__)